import numpy as np

class DBN:
    def __init__(self, states, transition_matrices, initial_state_distribution):
        """
        Constructor de la clase DBN.
        
        Args:
        - states: Lista de estados posibles en la DBN.
        - transition_matrices: Diccionario donde las claves son las transiciones y los valores son matrices de transición.
        - initial_state_distribution: Distribución de probabilidad inicial sobre los estados.
        """
        self.states = states
        self.transition_matrices = transition_matrices
        self.initial_state_distribution = initial_state_distribution

    def sample(self, n_steps):
        """
        Genera una secuencia de estados de la DBN utilizando muestreo aleatorio.

        Args:
        - n_steps: Número de pasos de tiempo para generar.

        Returns:
        - states_sequence: Lista de secuencia de estados generada.
        """
        states_sequence = []
        current_state = np.random.choice(self.states, p=self.initial_state_distribution)
        states_sequence.append(current_state)
        for _ in range(n_steps - 1):
            transition_matrix = self.transition_matrices[current_state]
            current_state = np.random.choice(self.states, p=transition_matrix[self.states.index(current_state)])
            states_sequence.append(current_state)
        return states_sequence

# Definimos los estados posibles
states = ['Sunny', 'Cloudy', 'Rainy']

# Definimos las matrices de transición
transition_matrices = {
    'Sunny': np.array([[0.8, 0.15, 0.05],
                       [0.4, 0.5, 0.1],
                       [0.2, 0.3, 0.5]]),
    'Cloudy': np.array([[0.6, 0.3, 0.1],
                        [0.3, 0.6, 0.1],
                        [0.2, 0.5, 0.3]]),
    'Rainy': np.array([[0.4, 0.3, 0.3],
                       [0.2, 0.3, 0.5],
                       [0.1, 0.2, 0.7]])
}

# Definimos la distribución inicial sobre los estados
initial_state_distribution = [0.6, 0.3, 0.1]

# Creamos una instancia de DBN
dbn = DBN(states, transition_matrices, initial_state_distribution)

# Generamos una secuencia de estados
sequence_length = 10
states_sequence = dbn.sample(sequence_length)

# Imprimimos la secuencia de estados generada
print("Secuencia de estados generada:")
print(states_sequence)