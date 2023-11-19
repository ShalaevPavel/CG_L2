
import cv2
import numpy as np


# Функция для применения высокочастотного фильтра (увеличение резкости)
def apply_high_pass_filter(image):
    kernel = np.array([[-1, -1, -1],
                       [-1, 9, -1],
                       [-1, -1, -1]])
    sharpened_image = cv2.filter2D(image, -1, kernel)
    return sharpened_image


# Функция для локальной пороговой обработки
def apply_local_thresholding(image):
    # Преобразование изображения в оттенки серого
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Применение адаптивного порога
    thresholded_image = cv2.adaptiveThreshold(gray_image, 255,
                                              cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                              cv2.THRESH_BINARY, 11, 2)
    return thresholded_image


# Загрузка изображения
image_path = 'img.jpg'
original_image = cv2.imread(image_path)

# Применение высокочастотного фильтра
sharpened_image = apply_high_pass_filter(original_image)

# Применение локальной пороговой обработки
thresholded_image = apply_local_thresholding(original_image)

# Отображение результатов
cv2.imshow('Original Image', original_image)
cv2.imshow('Sharpened Image', sharpened_image)
cv2.imshow('Thresholded Image', thresholded_image)

# Ожидание нажатия клавиши для закрытия окон
cv2.waitKey(0)
cv2.destroyAllWindows()
