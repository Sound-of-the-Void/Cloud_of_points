import cv2
import numpy as np
import open3d as o3d

def create_point_cloud_from_image(image):
    height, width, _ = image.shape
    points = []
    colors = []

    for y in range(height):
        for x in range(width):
            z = 0.5
            points.append([x, y, z])
            colors.append(image[y, x] / 255.0)  

    return np.array(points), np.array(colors)

def capture_image_from_camera():
    cap = cv2.VideoCapture(0)  

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру.")
        return None

    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Ошибка: Не удалось захватить изображение.")
        return None

    return frame

def main():
    image = capture_image_from_camera()

    if image is None:
        return

    points, colors = create_point_cloud_from_image(image)

    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.colors = o3d.utility.Vector3dVector(colors)

    # Визуализация облака точек
    o3d.visualization.draw_geometries([point_cloud], window_name="3D Point Cloud from Webcam Image")

if __name__ == "__main__":
    main()
