from constraint import Problem, AllDifferentConstraint

csp = Problem()
csp.addVariables(['A', 'B', 'C'], [1, 2, 3])
csp.addConstraint(AllDifferentConstraint())

def min_conflicts(csp, max_steps):
    assignment = {var: np.random.choice(csp.domains[var]) for var in csp.variables}
    for _ in range(max_steps):
        conflicted_vars = find_conflicted_vars(assignment, csp)
        if not conflicted_vars:
            return assignment
        var = np.random.choice(conflicted_vars)
        value = min_conflict_value(var, assignment, csp)
        assignment[var] = value
    return None

def find_conflicted_vars(assignment, csp):
    return [var for var in csp.variables if not is_consistent(assignment, var, assignment[var], csp)]

def min_conflict_value(var, assignment, csp):
    return min(csp.domains[var], key=lambda value: count_conflicts(var, value, assignment, csp))

def count_conflicts(var, value, assignment, csp):
    conflicts = 0
    for neighbor in csp.neighbors[var]:
        if neighbor in assignment and not is_consistent(assignment, neighbor, assignment[neighbor], csp):
            conflicts += 1
    return conflicts

# Ejemplo de uso
# csp = define el problema de satisfacción de restricciones
solution = min_conflicts(csp, max_steps=1000)
print("Solución encontrada:", solution)