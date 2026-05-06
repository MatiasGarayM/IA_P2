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

# Implementación de la iteración de políticas para resolver un MDP
def policy_iteration(mdp, epsilon):
    pi = {state: mdp.actions[state][0] for state in mdp.states}
    while True:
        V = evaluate_policy(pi, mdp, epsilon)
        policy_stable = True
        for state in mdp.states:
            if state not in mdp.terminal_states:
                old_action = pi[state]
                pi[state] = max(mdp.actions[state], key=lambda a: sum([p * (r + mdp.gamma * V[s_prime]) for (p, s_prime, r) in mdp.transitions[state][a]]))
                if old_action != pi[state]:
                    policy_stable = False
        if policy_stable:
            break
    return pi

V = policy_iteration(mdp, epsilon)
print("Valores óptimos:")
print(V)