import matplotlib.pyplot as plt
from simulation import simulate_mpc

def plot_results():
    time, spring_travel, velocity, deflection, unsprung, ctrl_effort = simulate_mpc()

    plt.figure(figsize=(12, 10), dpi=100)

    plt.subplot(411)
    plt.plot(time, spring_travel, 'r-', label='Suspension Travel', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Travel (m)')
    plt.title('Suspension Travel Over Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(412)
    plt.plot(time, velocity, 'r-', label='Sprung Mass Velocity', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Sprung Mass Velocity Over Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(413)
    plt.plot(time, deflection, 'r-', label='Wheel Deflection', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Deflection (m)')
    plt.title('Wheel Deflection Over Time')
    plt.grid(True)
    plt.legend()

    plt.subplot(414)
    plt.plot(time, unsprung, 'r-', label='Unsprung Mass Velocity', linewidth=2)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.title('Unsprung Mass Velocity Over Time')
    plt.grid(True)
    plt.legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_results()
