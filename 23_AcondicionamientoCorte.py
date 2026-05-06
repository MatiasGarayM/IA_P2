import numpy as np
from scipy.optimize import linprog

# Coeficientes de la función objetivo
c = [-4, -3]

# Coeficientes de las restricciones (lado izquierdo de las desigualdades)
A = [[2, 1], [1, 2]]

# Términos independientes de las restricciones (lado derecho de las desigualdades)
b = [14, 10]

# Aplicamos acondicionamiento del corte: Agregamos una nueva restricción que representa una combinación convexa de las restricciones originales
A = np.vstack([A, [1, 1]])  # Agregamos la restricción x1 + x2 <= M
b.append(20)  # Valor M: elija un valor suficientemente grande

# Resolvemos el problema de programación lineal utilizando el método simplex
result = linprog(c, A_ub=A, b_ub=b)

if result.success:
    print("Solución encontrada:")
    print("x1 =", result.x[0])
    print("x2 =", result.x[1])
    print("Valor óptimo de z =", -result.fun)  # Se usa -result.fun porque linprog minimiza la función objetivo
else:
    print("El problema no tiene solución óptima.")