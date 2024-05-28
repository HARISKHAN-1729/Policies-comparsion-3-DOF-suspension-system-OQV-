import numpy as np
import cvxpy as cp
from system_model_MPC import define_system

A_zoh, B_zoh = define_system()
nx, nu = B_zoh.shape
N = 10  # Prediction horizon
Q = np.diag([100, 1, 100, 1])
R = np.array([[0.1]])
x_desired = np.zeros(nx)

def run_mpc():
    x = cp.Variable((nx, N+1))
    u = cp.Variable((nu, N))
    x_init = cp.Parameter(nx)
    cost = 0
    constr = [x[:, 0] == x_init]
    for t in range(N):
        cost += cp.quad_form(x[:, t] - x_desired, Q) + cp.quad_form(u[:, t], R)
        constr += [cp.norm(u[:, t], 'inf') <= 10.]
        constr += [x[:, t + 1] == A_zoh @ x[:, t] + B_zoh @ u[:, t]]

    cost += cp.quad_form(x[:, N] - x_desired, Q)
    problem = cp.Problem(cp.Minimize(cost), constr)
    return problem, x_init, x, u
