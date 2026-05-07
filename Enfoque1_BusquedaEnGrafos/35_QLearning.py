import numpy as np

class QLearning:
    def __init__(self, num_states, num_actions, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        """
        Constructor de la clase QLearning.

        Args:
        - num_states: Número de estados posibles.
        - num_actions: Número de acciones posibles.
        - learning_rate: Tasa de aprendizaje (default=0.1).
        - discount_factor: Factor de descuento para futuras recompensas (default=0.9).
        - epsilon: Probabilidad de exploración (default=0.1).
        """
        self.num_states = num_states
        self.num_actions = num_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.q_table = np.zeros((num_states, num_actions))  # Inicializamos la tabla Q con ceros

    def choose_action(self, state):
        """
        Elige una acción utilizando una estrategia epsilon-greedy.

        Args:
        - state: Estado actual.

        Returns:
        - action: Acción seleccionada.
        """
        if np.random.rand() < self.epsilon:
            # Acción aleatoria con probabilidad epsilon
            action = np.random.randint(self.num_actions)
        else:
            # Acción óptima según la tabla Q
            action = np.argmax(self.q_table[state])
        return action

    def update_q_table(self, state, action, reward, next_state):
        """
        Actualiza la tabla Q según la regla de actualización de Q-learning.

        Args:
        - state: Estado actual.
        - action: Acción realizada.
        - reward: Recompensa obtenida.
        - next_state: Próximo estado.
        """
        current_q_value = self.q_table[state, action]
        next_max_q_value = np.max(self.q_table[next_state])
        new_q_value = current_q_value + self.learning_rate * (reward + self.discount_factor * next_max_q_value - current_q_value)
        self.q_table[state, action] = new_q_value

num_states = 5
num_actions = 2
num_episodes = 1000

q_learning_agent = QLearning(num_states, num_actions)

for episode in range(num_episodes):
    state = np.random.randint(num_states)  # Estado inicial aleatorio
    total_reward = 0
    while True:
        action = q_learning_agent.choose_action(state)
        # Simulación de la ejecución de la acción y obtención de la recompensa
        reward = np.random.normal(loc=0, scale=1)  # Recompensa aleatoria (ejemplo)
        next_state = (state + 1) % num_states  # Transición de estado (ejemplo)
        q_learning_agent.update_q_table(state, action, reward, next_state)
        total_reward += reward
        state = next_state
        if state == 0:  # Si llegamos al estado final, terminamos el episodio
            break
    print(f"Recompensa total en el episodio {episode + 1}: {total_reward}")

print("Tabla Q aprendida:")
print(q_learning_agent.q_table)