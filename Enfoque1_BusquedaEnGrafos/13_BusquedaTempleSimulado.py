import numpy as np
import matplotlib.pyplot as plt
import math

# Definimos la función
def f(x):
    return -(x - 2)**2 + 4

# Algoritmo de Temple Simulado
def simulated_annealing():
    current_x = np.random.uniform(0, 4)  # Empezamos desde un punto aleatorio en el dominio [0, 4]
    temperature = 1.0
    min_temperature = 0.0001
    cooling_rate = 0.99
    iterations = 0

    while temperature > min_temperature:
        iterations += 1
        next_x = current_x + np.random.uniform(-0.5, 0.5)  # Generamos un vecino aleatorio
        delta_e = f(next_x) - f(current_x)  # Calculamos el cambio en la función objetivo

        # Si el nuevo estado es mejor, lo aceptamos
        if delta_e > 0:
            current_x = next_x
        # Si el nuevo estado es peor, lo aceptamos con una cierta probabilidad
        else:
            if np.random.rand() < math.exp(delta_e / temperature):
                current_x = next_x

        # Disminuimos la temperatura
        temperature *= cooling_rate

    return current_x, f(current_x), iterations

# Ejecutamos el algoritmo
best_x, max_value, iterations = simulated_annealing()

# Visualizamos la función y el máximo local encontrado
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = -(x-2)^2 + 4')
plt.scatter(best_x, max_value, color='red', label=f'Máximo local: x = {best_x:.2f}, f(x) = {max_value:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Búsqueda de Temple Simulado')
plt.legend()
plt.grid(True)
plt.show()

print(f'Máximo local encontrado en x = {best_x:.2f}, con un valor de f(x) = {max_value:.2f}')
print(f'Número de iteraciones: {iterations}')