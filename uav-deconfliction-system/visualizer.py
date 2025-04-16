import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_missions(primary, others, conflicts):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Primary
    xs, ys, zs = zip(*[wp[:3] for wp in primary['waypoints']])
    ax.plot(xs, ys, zs, label='Primary Drone', color='blue')

    # Others
    for drone in others:
        xs, ys, zs = zip(*[wp[:3] for wp in drone['waypoints']])
        ax.plot(xs, ys, zs, label=f"Drone {drone['id']}", linestyle='--')

    # Conflicts
    for c in conflicts:
        x, y, z = c['location']
        ax.scatter(x, y, z, color='red', s=50, label='Conflict')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('UAV Conflict Simulation')
    plt.legend()
    plt.show()
