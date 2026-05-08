import numpy as np

observaciones = 'hola'

# Definir el modelo dinámico
def modelo_dinamico(x, u):
    return 0.5 * x + 25 * x / (1 + x ** 2) + 8 * np.cos(1.2 * u)

# Realizar filtrado de partículas
n_particulas = 1000
x_estimado = np.zeros(n_particulas)
pesos = np.ones(n_particulas) / n_particulas
for t in range(1, len(observaciones)):
    # Predicción
    x_estimado = modelo_dinamico(x_estimado, observaciones[t-1])
    # Actualización
    innovacion = observaciones[t] - x_estimado
    pesos *= np.exp(-0.5 * (innovacion / 2)**2)  # Actualizar pesos usando likelihood
    pesos /= np.sum(pesos)  # Normalizar pesos

# Estimar el estado
x_estimado_final = np.sum(x_estimado * pesos)

print("Estado estimado:", x_estimado_final)