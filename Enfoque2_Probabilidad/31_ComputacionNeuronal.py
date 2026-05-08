import numpy as np

class Neurona:
    def __init__(self, n_entradas):
        # Inicializamos los pesos y el sesgo de la neurona de forma aleatoria
        self.pesos = np.random.rand(n_entradas)
        self.sesgo = np.random.rand()

    def activacion(self, entradas):
        # Calculamos la suma ponderada de las entradas y aplicamos la función de activación (en este caso, la función lineal)
        suma_ponderada = np.dot(entradas, self.pesos) + self.sesgo
        return suma_ponderada

# Creamos una neurona con 3 entradas
neurona = Neurona(3)

# Definimos las entradas
entradas = np.array([0.5, 0.3, 0.2])

# Calculamos la salida de la neurona
salida = neurona.activacion(entradas)
print("Salida de la neurona:", salida)