import pytesseract
from PIL import Image

# Cargar la imagen con el texto a reconocer
image_path = 'handwritten_text.png'
image = Image.open(image_path)

# Reconocer texto en la imagen utilizando Tesseract OCR
text = pytesseract.image_to_string(image)

# Mostrar el texto reconocido
print("Texto reconocido:")
print(text)