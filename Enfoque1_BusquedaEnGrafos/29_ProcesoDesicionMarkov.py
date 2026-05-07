
class MDP:
    def __init__(self, states, actions, transitions, rewards, terminal_states, gamma):
        self.states = states  # Conjunto de estados
        self.actions = actions  # Función de acciones: actions[state] devuelve las acciones posibles en un estado dado
        self.transitions = transitions  # Función de transiciones: transitions[state][action] devuelve las transiciones posibles desde un estado dado con una acción dada
        self.rewards = rewards  # Función de recompensas: rewards[state][action] devuelve la recompensa esperada en un estado dado con una acción dada
        self.terminal_states = terminal_states  # Conjunto de estados terminales
        self.gamma = gamma  # Factor de descuento

# Ejemplo de uso
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