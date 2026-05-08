import numpy as np
import matplotlib.pyplot as plt

class Perceptron:
    def __init__(self, n_entradas, tasa_aprendizaje=0.01, epocas=100):
        self.n_entradas = n_entradas
        self.tasa_aprendizaje = tasa_aprendizaje
        self.epocas = epocas
        self.pesos = np.zeros(n_entradas + 1)  # +1 para el sesgo
    
    def predict(self, entradas):
        suma_ponderada = np.dot(entradas, self.pesos[1:]) + self.pesos[0]  # Producto punto de las entradas y pesos + sesgo
        return 1 if suma_ponderada > 0 else 0  # Función de activación: 1 si la suma ponderada es > 0, 0 en otro caso
    
    def entrenar(self, X, y):
        for _ in range(self.epocas):
            for entradas, etiqueta in zip(X, y):
                prediccion = self.predict(entradas)
                self.pesos[1:] += self.tasa_aprendizaje * (etiqueta - prediccion) * entradas
                self.pesos[0] += self.tasa_aprendizaje * (etiqueta - prediccion)


# Definir una función para generar puntos aleatorios en un plano
def generar_puntos(n):
    X = np.random.uniform(-10, 10, (n, 2))
    y = np.zeros(n)
    for i in range(n):
        # Definir una línea imaginaria (y = mx + b)
        m = 2  # Pendiente de la línea
        b = 3  # Intercepto de la línea
        # Asignar la etiqueta 1 si el punto está por encima de la línea, 0 si está por debajo
        if X[i, 1] > m * X[i, 0] + b:
            y[i] = 1
    return X, y

# Generar 100 puntos aleatorios
X, y = generar_puntos(100)

# Crear una instancia del Perceptrón
perceptron = Perceptron(n_entradas=2, tasa_aprendizaje=0.01, epocas=100)

# Entrenar el Perceptrón
perceptron.entrenar(X, y)

# Función para visualizar los puntos y la línea de separación del Perceptrón
def visualizar(X, y, perceptron):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
    plt.title('Clasificación de Puntos por el Perceptrón')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')

    # Dibujar la línea de separación del Perceptrón
    xmin, xmax = plt.xlim()
    pesos = perceptron.pesos
    ymin = (-pesos[0] - pesos[1] * xmin) / pesos[2]
    ymax = (-pesos[0] - pesos[1] * xmax) / pesos[2]
    plt.plot([xmin, xmax], [ymin, ymax], color='red')

    plt.show()

# Visualizar los puntos y la línea de separación del Perceptrón
visualizar(X, y, perceptron)