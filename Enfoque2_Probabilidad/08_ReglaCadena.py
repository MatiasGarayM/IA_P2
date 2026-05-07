import numpy as np

# Definir las probabilidades condicionales
p_A = np.array([0.3, 0.7])
p_B_dado_A = np.array([[0.2, 0.8], [0.6, 0.4]])

# Calcular la probabilidad conjunta P(A, B) utilizando la Regla de la Cadena
p_A_B = np.dot(p_A, p_B_dado_A)

print("Probabilidad conjunta P(A, B):")
print(p_A_B)