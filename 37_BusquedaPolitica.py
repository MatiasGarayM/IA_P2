import numpy as np

class PolicyIteration:
    def __init__(self, num_states, num_actions, transition_matrix, reward_matrix, discount_factor=0.9, epsilon=1e-6):
        self.num_states = num_states
        self.num_actions = num_actions
        self.transition_matrix = transition_matrix
        self.reward_matrix = reward_matrix
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.policy = np.zeros(num_states, dtype=int)  # Política inicial: todas las acciones son 0
        self.values = np.zeros(num_states)  # Valores de utilidad de los estados

    def policy_evaluation(self):
        """
        Realiza la evaluación de la política para calcular los valores de utilidad de los estados.

        Returns:
        - values: Valores de utilidad de los estados.
        """
        while True:
            delta = 0
            for state in range(self.num_states):
                new_value = 0
                for action in range(self.num_actions):
                    # Suma ponderada de las recompensas y los valores de utilidad de los estados siguientes
                    new_value += self.policy[state] == action * (np.sum(self.transition_matrix[state, action] * (self.reward_matrix[state, action] + 
                                                                                                                self.discount_factor * self.values)))
                delta = max(delta, np.abs(new_value - self.values[state]))
                self.values[state] = new_value
            if delta < self.epsilon:
                break
        return self.values

    def policy_improvement(self):
        """
        Realiza la mejora de la política basada en los valores de utilidad calculados.

        Returns:
        - policy_stable: Booleano que indica si la política ha convergido o no.
        """
        policy_stable = True
        for state in range(self.num_states):
            old_action = self.policy[state]
            action_values = np.zeros(self.num_actions)
            for action in range(self.num_actions):
                action_values[action] = np.sum(self.transition_matrix[state, action] * (self.reward_matrix[state, action] + 
                                                                                         self.discount_factor * self.values))
            self.policy[state] = np.argmax(action_values)  # Seleccionamos la acción con el mayor valor de utilidad
            if old_action != self.policy[state]:
                policy_stable = False
        return policy_stable

    def policy_iteration(self):
        """
        Realiza la iteración de políticas para encontrar la política óptima.

        Returns:
        - policy: Política óptima.
        """
        while True:
            self.policy_evaluation()
            if self.policy_improvement():
                break
        return self.policy

# Definimos los parámetros del entorno
num_states = 3
num_actions = 2
transition_matrix = np.array([[[0.8, 0.2, 0.0], [0.1, 0.7, 0.2]], [[0.2, 0.8, 0.0], [0.4, 0.4, 0.2]], [[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]]])
reward_matrix = np.array([[1.0, 2.0], [3.0, 0.0], [0.0, 0.0]])

# Creamos una instancia de PolicyIteration
policy_iteration = PolicyIteration(num_states, num_actions, transition_matrix, reward_matrix)

# Ejecutamos la iteración de políticas para encontrar la política óptima
optimal_policy = policy_iteration.policy_iteration()

print("Política óptima encontrada:")
print(optimal_policy)