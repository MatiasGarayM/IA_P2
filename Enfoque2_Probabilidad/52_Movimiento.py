import cv2

# Capturar video desde la cámara
cap = cv2.VideoCapture(0)

# Capturar el primer frame
ret, frame_prev = cap.read()
gray_prev = cv2.cvtColor(frame_prev, cv2.COLOR_BGR2GRAY)

while True:
    # Capturar el siguiente frame
    ret, frame_next = cap.read()
    gray_next = cv2.cvtColor(frame_next, cv2.COLOR_BGR2GRAY)

    # Calcular la diferencia absoluta entre los frames
    frame_diff = cv2.absdiff(gray_prev, gray_next)

    # Aplicar un umbral para resaltar las áreas de movimiento
    _, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

    # Encontrar contornos de las áreas de movimiento
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dibujar los contornos en el frame original
    cv2.drawContours(frame_next, contours, -1, (0, 255, 0), 2)

    # Mostrar el frame con las áreas de movimiento resaltadas
    cv2.imshow('Motion Detection', frame_next)

    # Actualizar el frame anterior
    gray_prev = gray_next.copy()

    # Salir si se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la captura y cerrar las ventanas
cap.release()
cv2.destroyAllWindows()