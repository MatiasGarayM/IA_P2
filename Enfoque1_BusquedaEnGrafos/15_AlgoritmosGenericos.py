import numpy as np
import matplotlib.pyplot as plt

# Definimos la función
def f(x):
    return -(x - 2)**2 + 4

# Definimos la clase para el problema de optimización
class OptimizationProblem:
    def __init__(self, min_x, max_x):
        self.min_x = min_x
        self.max_x = max_x

    def generate_random_solution(self):
        return np.random.uniform(self.min_x, self.max_x)

    def crossover(self, parent1, parent2, crossover_rate):
        if np.random.rand() < crossover_rate:
            return (parent1 + parent2) / 2  # Punto medio de los padres
        else:
            return parent1  # No se aplica crossover

    def mutate(self, solution):
        return solution + np.random.uniform(-0.5, 0.5)  # Mutación aleatoria

    def get_fitness(self, solution):
        return f(solution)

# Algoritmo de Algoritmos Genéticos
def genetic_algorithm(problem, population_size, crossover_rate, mutation_rate, max_iterations):
    population = [problem.generate_random_solution() for _ in range(population_size)]
    for _ in range(max_iterations):
        new_population = []
        for _ in range(population_size):
            parent1, parent2 = np.random.choice(population, size=2, replace=False)
            child = problem.crossover(parent1, parent2, crossover_rate)
            if np.random.rand() < mutation_rate:
                child = problem.mutate(child)
            new_population.append(child)
        population = new_population
    return max(population, key=problem.get_fitness)

# Definimos el problema de optimización
problem = OptimizationProblem(min_x=0, max_x=4)

# Ejecutamos el algoritmo genético
best_solution = genetic_algorithm(problem, population_size=50, crossover_rate=0.8, mutation_rate=0.1, max_iterations=100)

# Visualizamos la función y la mejor solución encontrada
x_values = np.linspace(0, 4, 100)
y_values = f(x_values)
plt.plot(x_values, y_values, label='f(x) = -(x-2)^2 + 4')
plt.scatter(best_solution, f(best_solution), color='red', label=f'Mejor solución: x = {best_solution:.2f}, f(x) = {f(best_solution):.2f}')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Algoritmos Genéticos')
plt.legend()
plt.grid(True)
plt.show()

print(f'Mejor solución encontrada en x = {best_solution:.2f}, con un valor de f(x) = {f(best_solution):.2f}')
