import numpy as np  

class PIDController:
    """A proportional-integral-derivative controller class."""
    def __init__(self, Kp, Ki, Kd, setpoint=0, output_limits=(-1000, 1000)):
        """Initialize the PID controller with gains and operational limits."""
        self.Kp = Kp  # Proportional gain
        self.Ki = Ki  # Integral gain
        self.Kd = Kd  # Derivative gain
        self.setpoint = setpoint  # Desired setpoint value
        self.integral = 0  # Integral sum starts at zero
        self.last_error = 0  # Keep track of previous error
        self.output_limits = output_limits  # Output limits (min, max)

    def update(self, measurement, dt):
        """Calculate PID output using measured error, considering derivative and integral terms."""
        error = self.setpoint - measurement  # Current error
        self.integral += error * dt  # Update integral
        derivative = (error - self.last_error) / dt  # Derivative term
        self.last_error = error  # Update last error
        output = (self.Kp * error + self.Ki * self.integral + self.Kd * derivative)  # PID formula
        output = max(min(output, self.output_limits[1]), self.output_limits[0])  # Apply output limits
        return output

class LQRController:
    """A linear-quadratic regulator controller class."""
    def __init__(self, K, setpoint=0):
        """Initialize the LQR controller with a gain matrix and a setpoint."""
        self.K = K  # State feedback gain matrix
        self.setpoint = np.array([setpoint] * len(K))  # Desired setpoint as an array

    def update(self, x):
        """Calculate the control action based on state deviation from setpoint."""
        return -np.dot(self.K, x - self.setpoint)  # Control law: u = -K(x - setpoint)
