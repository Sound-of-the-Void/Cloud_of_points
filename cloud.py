import numpy as np
import open3d as o3d
import matplotlib.pyplot as plt


def generate_point_cloud(num_points=1000):
    points = np.random.rand(num_points, 3)
    return points


def generate_camera_trajectory(num_frames=100):
    t = np.linspace(0, 10 * np.pi, num_frames)
    x = np.sin(t)
    y = np.cos(t)
    z = t / (10 * np.pi)
    return np.vstack((x, y, z)).T

def main():
    point_cloud_data = generate_point_cloud()
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(point_cloud_data)

    camera_trajectory = generate_camera_trajectory()

    o3d.visualization.draw_geometries([point_cloud], window_name="Point Cloud")

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(camera_trajectory[:, 0], camera_trajectory[:, 1], camera_trajectory[:, 2], color='r',
            label='Camera Trajectory')
    ax.scatter(point_cloud_data[:, 0], point_cloud_data[:, 1], point_cloud_data[:, 2], s=1, label='Point Cloud',
               alpha=0.5)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.legend()
    plt.title("Camera Trajectory and Point Cloud")
    plt.show()


if __name__ == "__main__":
    main()

