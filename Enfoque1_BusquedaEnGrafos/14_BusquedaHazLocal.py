import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def f(x):
    return -(x - 2)**2 + 4

# Algoritmo de Búsqueda de Haz Local
def beam_search(beam_width, max_iterations):
    current_states = np.random.uniform(0, 4, beam_width)  # Inicializamos estados aleatorios
    best_x = current_states[0]
    for _ in range(max_iterations):
        next_states = []
        for current_x in current_states:
            neighbors = [current_x + dx for dx in [-0.1, 0.1]]  # Generamos vecinos izquierda y derecha
            next_states.extend(neighbors)
        next_states = sorted(next_states, key=f, reverse=True)[:beam_width]  # Seleccionamos los mejores estados
        current_states = next_states
        if f(current_states[0]) > f(best_x):
            best_x = current_states[0]
    return best_x, f(best_x)

# Ejecutamos el algoritmo
best_x, max_value = beam_search(beam_width=5, max_iterations=100)

# Visualizamos la función y el máximo local encontrado
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = -(x-2)^2 + 4')
plt.scatter(best_x, max_value, color='red', label=f'Máximo local: x = {best_x:.2f}, f(x) = {max_value:.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Búsqueda de Haz Local')
plt.legend()
plt.grid(True)
plt.show()

print(f'Máximo local encontrado en x = {best_x:.2f}, con un valor de f(x) = {max_value:.2f}')
