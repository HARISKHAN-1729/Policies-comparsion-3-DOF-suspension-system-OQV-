import numpy as np
from mpc_control import run_mpc
from system_model_MPC import define_system

def simulate_mpc(nsim=100):
    A_zoh, B_zoh = define_system()
    problem, x_init, x, u = run_mpc()
    dt = 1/10

    x0 = np.array([0.05, 0, -0.05, 0])
    time = [0.]
    spring_travel = [x0[0]]
    velocity = [x0[1]]
    deflection = [x0[2]]
    unsprung = [x0[3]]
    ctrl_effort = []

    for i in range(1, nsim+1):
        x_init.value = x0
        problem.solve(solver=cp.OSQP, warm_start=True)

        x0 = A_zoh.dot(x0) + B_zoh.dot(u[:, 0].value)
        time.append(i * dt)
        spring_travel.append(x0[0])
        velocity.append(x0[1])
        deflection.append(x0[2])
        unsprung.append(x0[3])
        ctrl_effort.append(u[:, 0].value)

    return time, spring_travel, velocity, deflection, unsprung, ctrl_effort

if __name__ == "__main__":
    time, spring_travel, velocity, deflection, unsprung, ctrl_effort = simulate_mpc()
