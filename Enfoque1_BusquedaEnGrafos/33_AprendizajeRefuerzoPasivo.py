import numpy as np

# Definimos una función para el aprendizaje por refuerzo pasivo
def passive_learning(rewards, transitions, discount_factor, epsilon, num_episodes):
    """
    Realiza el aprendizaje por refuerzo pasivo utilizando la estrategia epsilon-greedy.

    Args:
    - rewards: Matriz de recompensas (número de estados x número de acciones).
    - transitions: Matriz de transiciones de estado (número de estados x número de acciones x número de estados).
    - discount_factor: Factor de descuento para futuras recompensas.
    - epsilon: Probabilidad de elegir una acción aleatoria en lugar de la mejor acción.
    - num_episodes: Número de episodios de entrenamiento.
    """
    num_states, num_actions, _ = transitions.shape
    policy = np.zeros((num_states, num_actions))  # Inicializamos la política uniformemente
    for _ in range(num_episodes):
        state = np.random.randint(num_states)  # Seleccionamos un estado aleatorio para comenzar el episodio
        while True:
            if np.random.rand() < epsilon:
                action = np.random.randint(num_actions)  # Seleccionamos una acción aleatoria con probabilidad epsilon
            else:
                action = np.argmax(policy[state])  # Elegimos la mejor acción según la política actual
            next_state = np.random.choice(num_states, p=transitions[state, action])  # Transición de estado según la acción elegida
            reward = rewards[state, action]  # Recompensa obtenida por la acción
            policy[state, action] += reward  # Actualizamos la política basada en la recompensa
            state = next_state  # Actualizamos el estado para el próximo paso
            if state == num_states - 1:  # Si llegamos al estado final, terminamos el episodio
                break
    policy /= num_episodes  # Normalizamos la política dividiendo por el número de episodios
    return policy

# Ejemplo de uso
# Define las matrices de recompensas y transiciones según el entorno específico
rewards = ...
transitions = ...
discount_factor = 0.9
epsilon = 0.1
num_episodes = 1000
policy = passive_learning(rewards, transitions, discount_factor, epsilon, num_episodes)
print("Política aprendida:")
print(policy)