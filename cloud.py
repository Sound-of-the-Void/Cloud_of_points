import cv2
import numpy as np
import open3d as o3d

# Функция для создания облака точек на основе цветового изображения
def create_point_cloud_from_image(image):
    height, width, _ = image.shape
    points = []
    colors = []

    # Генерация 3D координат и соответствующих цветов
    for y in range(height):
        for x in range(width):
            z = 0.5  # Упрощенная постоянная глубина (можно заменить на более продвинутые методы)
            points.append([x, y, z])
            colors.append(image[y, x] / 255.0)  # Нормализация цвета

    return np.array(points), np.array(colors)

# Функция для захвата изображения из веб-камеры
def capture_image_from_camera():
    cap = cv2.VideoCapture(0)  # Открытие веб-камеры

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру.")
        return None

    ret, frame = cap.read()
    cap.release()  # Освобождение камеры после захвата

    if not ret:
        print("Ошибка: Не удалось захватить изображение.")
        return None

    return frame

# Основная функция
def main():
    # Захват изображения с веб-камеры
    image = capture_image_from_camera()

    if image is None:
        return

    # Создание облака точек из захваченного изображения
    points, colors = create_point_cloud_from_image(image)

    # Создание облака точек в Open3D
    point_cloud = o3d.geometry.PointCloud()
    point_cloud.points = o3d.utility.Vector3dVector(points)
    point_cloud.colors = o3d.utility.Vector3dVector(colors)

    # Визуализация облака точек
    o3d.visualization.draw_geometries([point_cloud], window_name="3D Point Cloud from Webcam Image")

if __name__ == "__main__":
    main()