import speech_recognition as sr
import pyaudio

# Inicializar el reconocedor
r = sr.Recognizer()

# Capturar audio del micrófono
with sr.Microphone() as source:
    print("Diga algo...")
    audio = r.listen(source)

# Realizar reconocimiento del habla
try:
    texto = r.recognize_google(audio)
    print("Google Speech Recognition ha entendido:", texto)
except sr.UnknownValueError:
    print("Google Speech Recognition no pudo entender el audio")
except sr.RequestError as e:
    print("No se pudo obtener respuesta de Google Speech Recognition; {0}".format(e))