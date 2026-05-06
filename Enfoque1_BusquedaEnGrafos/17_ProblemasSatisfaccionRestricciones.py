from constraint import Problem, AllDifferentConstraint

# Creamos un problema de satisfacción de restricciones
problem = Problem()

# Definimos las variables y sus dominios
problem.addVariables(['A', 'B', 'C'], [1, 2, 3])

# Definimos las restricciones
problem.addConstraint(AllDifferentConstraint())

# Encontramos una solución
solutions = problem.getSolutions()
print("Soluciones encontradas:")
for solution in solutions:
    print(solution)