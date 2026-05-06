import random
import time

def online_search(target):
    while True:
        guess = random.randint(1, 100)  # Supongamos que estamos buscando un número entre 1 y 100
        print("Intentando:", guess)
        if guess == target:
            print("¡Objetivo alcanzado! El número buscado es:", guess)
            return
        time.sleep(1)  # Simulación de tiempo de espera antes de realizar el próximo intento

# Ejemplo de uso
target_number = random.randint(1, 100)  # Generamos un número aleatorio como objetivo
print("Número objetivo:", target_number)
print("Iniciando búsqueda en línea...")
online_search(target_number)
