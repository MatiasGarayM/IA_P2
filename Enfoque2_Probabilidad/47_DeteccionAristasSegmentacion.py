import cv2

# Cargar imagen en escala de grises
image = cv2.imread('input_image.jpg', cv2.IMREAD_GRAYSCALE)

# Detectar bordes utilizando el operador Canny
edges = cv2.Canny(image, 100, 200)

# Mostrar imágenes
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detection', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()