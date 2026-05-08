import numpy as np
from filterpy.kalman import KalmanFilter

# Definir el filtro de Kalman
kf = KalmanFilter(dim_x=2, dim_z=1)

# Definir las matrices de transición y de observación
kf.F = np.array([[1, 1], [0, 1]])  # Matriz de transición
kf.H = np.array([[1, 0]])           # Matriz de observación

# Definir las matrices de covarianza del proceso y de la medición
kf.Q *= 0.01  # Covarianza del proceso
kf.R *= 0.1   # Covarianza de la medición

# Estimar el estado utilizando una serie de observaciones
observaciones = np.array([1, 2, 3, 4, 5])
for z in observaciones:
    kf.predict()
    kf.update(z)

print("Estado estimado:", kf.x)