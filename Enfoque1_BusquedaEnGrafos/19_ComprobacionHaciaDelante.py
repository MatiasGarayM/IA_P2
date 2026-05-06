from constraint import Problem, AllDifferentConstraint

csp = Problem()
csp.addVariables(['A', 'B', 'C'], [1, 2, 3])
csp.addConstraint(AllDifferentConstraint())

def forward_checking(assignment, csp):
    if len(assignment) == len(csp.variables):
        return assignment
    var = select_unassigned_variable(assignment, csp)
    for value in csp.domains[var]:
        if is_consistent(assignment, var, value, csp):
            assignment[var] = value
            inferences = {}
            for neighbor in csp.neighbors[var]:
                if neighbor not in assignment:
                    for neighbor_value in csp.domains[neighbor]:
                        if neighbor_value != value:
                            inferences.setdefault(neighbor, []).append(neighbor_value)
            result = forward_checking(assignment, csp)
            if result is not None:
                return result
            del assignment[var]
            for k, v in inferences.items():
                csp.domains[k].extend(v)
    return None

assignment = {}

result = forward_checking(assignment, csp)
print("Solución encontrada:", result)