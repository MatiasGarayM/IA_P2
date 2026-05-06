class MDP:
    def __init__(self):
        self.states = {'S1', 'S2'}
        self.actions = {'S1': {'A1', 'A2'}, 'S2': {'A1', 'A2'}}
        self.transitions = {'S1': {'A1': [(0.8, 'S1', -1), (0.2, 'S2', 2)], 'A2': [(0.5, 'S1', -1), (0.5, 'S2', -3)]},
                            'S2': {'A1': [(0.3, 'S1', 0), (0.7, 'S2', 0)], 'A2': [(0.9, 'S1', 0), (0.1, 'S2', 0)]}}
        self.rewards = {'S1': {'A1': -1, 'A2': 2}, 'S2': {'A1': 0, 'A2': -3}}
        self.terminal_states = {'S2'}
        self.gamma = 0.9
mdp = MDP()

# Implementación de la iteración de valores para resolver un MDP
def value_iteration(mdp, epsilon):
    V = {state: 0 for state in mdp.states}
    while True:
        delta = 0
        for state in mdp.states:
            if state not in mdp.terminal_states:
                v = V[state]
                V[state] = max([sum([p * (r + mdp.gamma * V[s_prime]) for (p, s_prime, r) in mdp.transitions[state][action]]) for action in mdp.actions[state]])
                delta = max(delta, abs(v - V[state]))
        if delta < epsilon:
            break
    return V

# Ejemplo de uso
# mdp = define el Proceso de Decisión de Markov
# epsilon = tolerancia para la convergencia
V = value_iteration(mdp, epsilon)
print("Valores óptimos:")
print(V)