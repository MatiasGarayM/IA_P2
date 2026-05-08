import numpy as np

# Definir matriz de transición de la cadena de Markov
P = np.array([[0.8, 0.2], [0.4, 0.6]])

# Definir estado inicial
estado_actual = 0

# Simular la cadena de Markov
n = 10
secuencia_estados = [estado_actual]
for _ in range(n-1):
    estado_actual = np.random.choice([0, 1], p=P[estado_actual])
    secuencia_estados.append(estado_actual)

print("Secuencia de Estados:", secuencia_estados)