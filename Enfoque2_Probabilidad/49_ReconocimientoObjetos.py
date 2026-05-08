import cv2

# Cargar el clasificador de Haar para detección de caras
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Cargar la imagen
image = cv2.imread('input_image.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detectar caras en la imagen
faces = face_cascade.detectMultiScale(gray, 1.1, 4)

# Dibujar rectángulos alrededor de las caras detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)

# Mostrar la imagen con las caras detectadas
cv2.imshow('Detected Faces', image)
cv2.waitKey(0)
cv2.destroyAllWindows()