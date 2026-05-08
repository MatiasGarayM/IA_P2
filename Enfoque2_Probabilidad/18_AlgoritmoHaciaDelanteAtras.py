import numpy as np

# Definir modelo HMM
N = 2  # Número de estados ocultos
M = 3  # Número de observaciones posibles
T = 4  # Longitud de la secuencia de observaciones

pi = np.array([0.5, 0.5])  # Probabilidades iniciales de los estados
A = np.array([[0.7, 0.3], [0.4, 0.6]])  # Matriz de transición de estados
B = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])  # Matriz de emisión

# Observaciones
observaciones = np.array([0, 1, 2, 0])

# Algoritmo hacia adelante
alpha = np.zeros((T, N))
alpha[0] = pi * B[:, observaciones[0]]
for t in range(1, T):
    alpha[t] = np.dot(alpha[t - 1], A) * B[:, observaciones[t]]

# Algoritmo hacia atrás
beta = np.zeros((T, N))
beta[T - 1] = 1
for t in range(T - 2, -1, -1):
    beta[t] = np.dot(A, B[:, observaciones[t + 1]] * beta[t + 1])

# Calcular la probabilidad de la secuencia de observaciones
p_observaciones = np.sum(alpha[-1])

print("Probabilidad de la secuencia de observaciones:", p_observaciones)