import numpy as np
import matplotlib.pyplot as plt

# Parámetros del proceso AR
phi = 0.9
sigma = 1
n = 1000

# Generar una serie de tiempo estacionaria
np.random.seed(0)
epsilon = np.random.normal(0, sigma, n)
serie_tiempo = [epsilon[0]]
for i in range(1, n):
    serie_tiempo.append(phi * serie_tiempo[i-1] + epsilon[i])

# Graficar la serie de tiempo
plt.plot(serie_tiempo)
plt.title('Proceso AR(1) Estacionario')
plt.xlabel('Tiempo')
plt.ylabel('Valor')
plt.show()