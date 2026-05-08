import cv2
import numpy as np

# Cargar imagen
image = cv2.imread('input_image.jpg', cv2.IMREAD_COLOR)

# Aplicar filtro de desenfoque gaussiano
blurred_image = cv2.GaussianBlur(image, (5, 5), 0)

# Mostrar imágenes
cv2.imshow('Original Image', image)
cv2.imshow('Blurred Image', blurred_image)
cv2.waitKey(0)
cv2.destroyAllWindows()