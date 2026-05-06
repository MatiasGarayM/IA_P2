import numpy as np

class EpsilonGreedy:
    def __init__(self, num_actions, epsilon=0.1):
        """
        Constructor de la clase EpsilonGreedy.

        Args:
        - num_actions: Número de acciones posibles.
        - epsilon: Probabilidad de exploración (default=0.1).
        """
        self.num_actions = num_actions
        self.epsilon = epsilon

    def choose_action(self, q_values):
        """
        Elige una acción utilizando la estrategia epsilon-greedy.

        Args:
        - q_values: Valores Q para cada acción.

        Returns:
        - action: Acción seleccionada.
        """
        if np.random.rand() < self.epsilon:
            # Acción aleatoria con probabilidad epsilon
            action = np.random.randint(self.num_actions)
        else:
            # Acción óptima según los valores Q
            action = np.argmax(q_values)
        return action

num_actions = 3
epsilon_greedy = EpsilonGreedy(num_actions)

# Supongamos que tenemos valores Q para cada acción
q_values = [0.5, 0.8, 0.3]

# Seleccionamos una acción utilizando la estrategia epsilon-greedy
chosen_action = epsilon_greedy.choose_action(q_values)
print("Acción seleccionada:", chosen_action)