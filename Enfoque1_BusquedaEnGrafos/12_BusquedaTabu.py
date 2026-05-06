import numpy as np
import matplotlib.pyplot as plt
from collections import deque

# Definimos la función
def f(x):
    return -(x - 2)**2 + 4

# Algoritmo de búsqueda tabú
def tabu_search():
    current_x = np.random.uniform(0, 4)  # Empezamos desde un punto aleatorio en el dominio [0, 4]
    tabu_list = deque(maxlen=5)  # Lista tabú de tamaño limitado
    best_x = current_x
    iterations = 0
    while True:
        iterations += 1
        neighbors = [current_x + dx for dx in [-0.1, 0.1]]  # Movimientos permitidos: izquierda y derecha
        neighbors = [(neighbor, f(neighbor)) for neighbor in neighbors if neighbor not in tabu_list]
        if not neighbors:  # Si todos los vecinos están en la lista tabú, detenemos la búsqueda
            break
        next_x, _ = max(neighbors, key=lambda x: x[1])  # Movemos a la posición con el valor más alto
        tabu_list.append(next_x)  # Añadimos el movimiento a la lista tabú
        current_x = next_x
        if f(next_x) > f(best_x):
            best_x = next_x
    return best_x, f(best_x), iterations

# Ejecutamos el algoritmo
best_x, max_value, iterations = tabu_search()

# Visualizamos la función y el máximo local encontrado
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = -(x-2)^2 + 4')
plt.scatter(best_x, max_value, color='red', label=f'Máximo local: x = {best_x:.2f}, f(x) = {max_value:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Búsqueda Tabú')
plt.legend()
plt.grid(True)
plt.show()

print(f'Máximo local encontrado en x = {best_x:.2f}, con un valor de f(x) = {max_value:.2f}')
print(f'Número de iteraciones: {iterations}')