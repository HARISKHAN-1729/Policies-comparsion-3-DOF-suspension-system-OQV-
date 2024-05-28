import numpy as np
import matplotlib.pyplot as plt

def load_results():
    """Load simulation results from the output file."""
    data = np.load('output/simulation_results.npz')
    return data['t'], data['y']

def plot_results(t, y):
    """Generate plots from the simulation results for both PID and LQR controllers."""
    plt.figure(figsize=(12, 10))

    # Plot for Sprung Mass Velocity
    plt.subplot(321)
    plt.plot(t, y[1], label='Sprung Mass Velocity (PID)', color='darkblue')
    plt.plot(t, y[5], label='Sprung Mass Velocity (LQR)', linestyle='dashed', color='red')
    plt.title("Sprung Mass Velocity")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend()
    plt.grid(True)

    # Plot for Wheel Vertical Velocity
    plt.subplot(322)
    plt.plot(t, y[3], label='Wheel Vertical Velocity (PID)', color='darkblue')
    plt.plot(t, y[7], label='Wheel Vertical Velocity (LQR)', linestyle='dashed', color='red')
    plt.title("Wheel Vertical Velocity")
    plt.xlabel("Time (s)")
    plt.ylabel("Velocity (m/s)")
    plt.legend()
    plt.grid(True)

    # Plot for Acceleration
    plt.subplot(323)
    a_s_pid = np.gradient(y[1], t)
    a_s_lqr = np.gradient(y[5], t)
    plt.plot(t, a_s_pid, label='Acceleration (PID)', color='darkblue')
    plt.plot(t, a_s_lqr, label='Acceleration (LQR)', linestyle='dashed', color='red')
    plt.title("Acceleration")
    plt.xlabel("Time (s)")
    plt.ylabel("Acceleration (m/s²)")
    plt.legend()
    plt.grid(True)

    # Plot for Wheel’s Deflection
    plt.subplot(324)
    plt.plot(t, y[2], label='Wheel’s Deflection (PID)', color='darkblue')
    plt.plot(t, y[6], label='Wheel’s Deflection (LQR)', linestyle='dashed', color='red')
    plt.title("Wheel’s Deflection")
    plt.xlabel("Time (s)")
    plt.ylabel("Deflection (m)")
    plt.legend()
    plt.grid(True)

    # Plot for Spring Travel
    plt.subplot(325)
    plt.plot(t, y[0], label='Spring Travel (PID)', color='darkblue')
    plt.plot(t, y[4], label='Spring Travel (LQR)', linestyle='dashed', color='red')
    plt.title("Spring Travel")
    plt.xlabel("Time (s)")
    plt.ylabel("Travel (m)")
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig('output/simulation_plots.png')
    plt.show()
    

def main():
    t, y = load_results()
    plot_results(t, y)

if __name__ == "__main__":
    main()
