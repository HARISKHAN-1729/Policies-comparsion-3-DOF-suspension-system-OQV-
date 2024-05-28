import numpy as np  

def calculate_cost(states, controls, Q, R, dt):
    """Calculate the trajectory cost using quadratic cost function."""
    J_hat = 0  # Initialize total cost
    n_steps = controls.shape[1]  # Number of steps in trajectory
    for i in range(n_steps):
        state_cost = np.dot(states[:, i].T, np.dot(Q, states[:, i]))  # Quadratic state cost
        control_cost = np.dot(controls[:, i].T, np.dot(R, controls[:, i]))  # Quadratic control cost
        J_hat += (state_cost + control_cost) * dt  # Accumulate total cost over time
    return J_hat  # Return total cost
