import numpy as np
from scipy.linalg import solve_continuous_are
from scipy.integrate import solve_ivp
import os
import tkinter as tk
from policies import PIDController, LQRController
from cost import calculate_cost

def ensure_directory(directory):
    """Ensure the output directory exists."""
    if not os.path.exists(directory):
        os.makedirs(directory)

def road_profile(t):
    """Define the road profile as a function of time."""
    t_start = 1
    t_stop = 1.09
    if t_start <= t <= t_stop:
        return 0.04 * (1 - np.cos(7 * np.pi * (t - t_start)))
    return 0

def quarter_car_model_combined(t, x, m_s, m_us, k_s, k_us, b_s, b_us, pid, lqr):
    """Define the dynamics of the quarter-car model for PID and LQR."""
    x1_pid, x2_pid, x3_pid, x4_pid, x1_lqr, x2_lqr, x3_lqr, x4_lqr = x
    z_r = road_profile(t)
    Zr_dot = (road_profile(t + 0.01) - z_r) / 0.01

    Fa_pid = pid.update(x1_pid, 0.01)
    Fa_lqr = lqr.update(np.array([x1_lqr, x2_lqr, x3_lqr, x4_lqr]))

    # Dynamics equations for PID controlled system
    dx1dt_pid = x2_pid - x4_pid
    dx2dt_pid = (-k_s * x1_pid - b_s * (x2_pid - x4_pid) + Fa_pid) / m_s
    dx3dt_pid = x4_pid - Zr_dot
    dx4dt_pid = (k_s * x1_pid + b_s * (x2_pid - x4_pid) - k_us * x3_pid - b_us * (x4_pid - Zr_dot)) / m_us

    # Dynamics equations for LQR controlled system
    dx1dt_lqr = x2_lqr - x4_lqr
    dx2dt_lqr = (-k_s * x1_lqr - b_s * (x2_lqr - x4_lqr) + Fa_lqr) / m_s
    dx3dt_lqr = x4_lqr - Zr_dot
    dx4dt_lqr = (k_s * x1_lqr + b_s * (x2_lqr - x4_lqr) - k_us * x3_lqr - b_us * (x4_lqr - Zr_dot)) / m_us

    return [dx1dt_pid, dx2dt_pid, dx3dt_pid, dx4dt_pid, dx1dt_lqr, dx2dt_lqr, dx3dt_lqr, dx4dt_lqr]


def main():

    ensure_directory('output')  # Ensure the output directory exists

    m_s, m_us, k_s, k_us, b_s, b_us = 234, 43, 26000, 100000, 1544, 0
    pid = PIDController(Kp=10000, Ki=50, Kd=400, setpoint=0, output_limits=(-1000, 1000))

    # Matrix A and B for LQR setup
    A = np.array([
        [0, 1, 0, -1],
        [-k_s/m_s, -b_s/m_s, 0, b_s/m_s],
        [0, 0, 0, 1],
        [k_s/m_us, (b_s)/m_us, -k_us/m_us, (-b_s-b_us)/m_us]
    ])
    B = np.array([
        [0, 1/m_s, 0, -1/m_us]
    ]).T
    Q = np.diag([4, 3, 5, 10])
    R = np.array([[0.0009]])

    P = solve_continuous_are(A, B, Q, R)
    K = np.dot(np.linalg.inv(R), np.dot(B.T, P))

    lqr = LQRController(K=K[0])


    x0_extended = [0.01, 0.02, 0.01, 0.02, 0.01, 0.02, 0.01, 0.02]
    t_span = (0, 5)
    t_eval = np.linspace(t_span[0], t_span[1], 500)
    solution = solve_ivp(lambda t, x: quarter_car_model_combined(t, x, m_s, m_us, k_s, k_us, b_s, b_us, pid, lqr),
                         t_span, x0_extended, t_eval=t_eval, method='RK45')
    

    dt = np.mean(np.diff(t_eval))




    controls_pid = np.array([pid.update(measurement, 0.01) for measurement in  solution.y[0]])
    controls_pid = controls_pid.reshape(1, -1)
    states_pid = np.vstack((solution.y[0], np.gradient(solution.y[1], solution.t), solution.y[2], solution.y[3]))
    cost_pid = calculate_cost(states_pid, controls_pid, Q, R, dt)
    print("Approximate trajectory cost for PID: {:.2f}".format(cost_pid))
   


    
    states = np.array([solution.y[4],np.gradient(solution.y[5], solution.t) , solution.y[6], solution.y[7]])
    controls = np.array([lqr.update(states[:, i]) for i in range(states.shape[1] - 1)])
    controls = controls.reshape(1, -1)
    cost = calculate_cost(states, controls, Q, R, dt)
    print("Approximate trajectory cost LQR: {:.2f}".format(cost)) 



    np.savez('output/simulation_results.npz', t=solution.t, y=solution.y)



if __name__ == "__main__":
    main()
