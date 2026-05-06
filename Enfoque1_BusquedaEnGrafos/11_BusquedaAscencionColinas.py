import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def f(x):
    return -x**2 + 4*x

# Definimos la derivada de la función (para encontrar la pendiente)
def f_derivative(x):
    return -2*x + 4

# Algoritmo de ascenso de colinas
def hill_climbing():
    # Empezamos desde un punto aleatorio en el dominio [0, 4]
    current_x = np.random.uniform(0, 4)
    iterations = 0
    while True:
        iterations += 1
        gradient = f_derivative(current_x)
        if abs(gradient) < 0.001:  # Condición de convergencia
            break
        # Movemos hacia arriba en la dirección de la pendiente
        current_x = current_x + 0.1 * gradient  # Tasa de aprendizaje = 0.1
    return current_x, f(current_x), iterations

# Ejecutamos el algoritmo
max_x, max_value, iterations = hill_climbing()

# Visualizamos la función y el máximo local encontrado
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = -x^2 + 4x')
plt.scatter(max_x, max_value, color='red', label=f'Máximo local: x = {max_x:.2f}, f(x) = {max_value:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Búsqueda de Ascenso de Colinas')
plt.legend()
plt.grid(True)
plt.show()

print(f'Máximo local encontrado en x = {max_x:.2f}, con un valor de f(x) = {max_value:.2f}')
print(f'Número de iteraciones: {iterations}')