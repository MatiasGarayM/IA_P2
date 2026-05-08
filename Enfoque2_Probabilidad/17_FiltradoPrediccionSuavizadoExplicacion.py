import numpy as np
from scipy.linalg import block_diag

# Definir modelo de espacio de estado (predicción de una caminata aleatoria)
F = np.array([[1]])
G = np.array([[1]])
H = np.array([[1]])
Q = np.array([[0.1]])
R = np.array([[0.5]])

# Generar observaciones
np.random.seed(0)
n = 10
observaciones = np.random.normal(0, np.sqrt(R[0, 0]), n)

# Predicción utilizando filtro de Kalman
x_pred = np.zeros(n)  # Vector de predicciones
P_pred = np.zeros(n)  # Varianza de las predicciones
x = np.zeros(n)       # Vector de estados estimados
P = np.zeros(n)       # Varianza de los estados estimados

x[0] = 0
P[0] = 0.1
for i in range(1, n):
    # Predicción
    x_pred[i] = F.dot(x[i-1])
    P_pred[i] = F.dot(P[i-1]).dot(F.T) + G.dot(Q).dot(G.T)

    # Actualización
    K = P_pred[i].dot(H.T).dot(np.linalg.inv(H.dot(P_pred[i]).dot(H.T) + R))
    x[i] = x_pred[i] + K.dot(observaciones[i] - H.dot(x_pred[i]))
    P[i] = (np.eye(1) - K.dot(H)).dot(P_pred[i])

print("Predicciones:", x_pred)
print("Estados Estimados:", x)