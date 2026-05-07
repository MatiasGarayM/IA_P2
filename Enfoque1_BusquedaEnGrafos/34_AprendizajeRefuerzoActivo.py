import numpy as np

class ActiveRL:
    def __init__(self, num_actions):
        """
        Constructor de la clase ActiveRL.

        Args:
        - num_actions: Número de acciones posibles.
        """
        self.num_actions = num_actions
        self.action_counts = np.zeros(num_actions)  # Contador de visitas a cada acción
        self.action_rewards = np.zeros(num_actions)  # Recompensa acumulada de cada acción

    def ucb_action(self, t):
        """
        Calcula la acción según el algoritmo UCB en el tiempo t.

        Args:
        - t: Paso de tiempo actual.

        Returns:
        - action: Acción seleccionada.
        """
        ucb_values = self.action_rewards / self.action_counts + np.sqrt(2 * np.log(t) / (self.action_counts + 1e-6))
        return np.argmax(ucb_values)

    def update(self, action, reward):
        """
        Actualiza los contadores de acción y recompensa.

        Args:
        - action: Acción realizada.
        - reward: Recompensa obtenida.
        """
        self.action_counts[action] += 1
        self.action_rewards[action] += reward

num_actions = 3
active_rl = ActiveRL(num_actions)

num_episodes = 1000
reward_per_episode = []

for episode in range(num_episodes):
    # Seleccionamos una acción utilizando UCB
    action = active_rl.ucb_action(episode + 1)  # +1 para evitar divisiones por cero
    # Simulamos la ejecución de la acción y obtenemos una recompensa
    reward = np.random.normal(loc=0, scale=1)  # Recompensa aleatoria (ejemplo)
    # Actualizamos los contadores de acción y recompensa
    active_rl.update(action, reward)
    # Almacenamos la recompensa acumulada por episodio para análisis posterior
    reward_per_episode.append(reward)

print("Recompensa acumulada por episodio:")
print(reward_per_episode)