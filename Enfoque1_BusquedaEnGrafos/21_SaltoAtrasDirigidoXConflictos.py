from constraint import Problem, AllDifferentConstraint

csp = Problem()
csp.addVariables(['A', 'B', 'C'], [1, 2, 3])
csp.addConstraint(AllDifferentConstraint())

def conflict_directed_backjumping(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in csp.domains[var]:
        assignment[var] = value
        if is_consistent(assignment, csp):
            result = conflict_directed_backjumping(assignment, csp)
            if result is not None:
                return result
        del assignment[var]
    return None

assignment = {}
result = conflict_directed_backjumping(assignment, csp)
print("Solución encontrada:", result)