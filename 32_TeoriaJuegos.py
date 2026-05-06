import numpy as np

# Ejemplo de cálculo de equilibrio de Nash en un juego de dos jugadores
payoff_matrix_player1 = np.array([[3, 1], [2, 2]])
payoff_matrix_player2 = np.array([[2, 1], [1, 3]])

# Función para encontrar el equilibrio de Nash en un juego de dos jugadores
def find_nash_equilibrium(payoff_matrix):
    max_payoff_indices = np.argwhere(payoff_matrix == np.amax(payoff_matrix))
    nash_equilibrium = [(max_payoff_indices[0][0], max_payoff_indices[0][1])]
    for i in range(1, len(max_payoff_indices)):
        if max_payoff_indices[i][0] != nash_equilibrium[0][0]:
            break
        nash_equilibrium.append((max_payoff_indices[i][0], max_payoff_indices[i][1]))
    return nash_equilibrium

nash_equilibrium_player1 = find_nash_equilibrium(payoff_matrix_player1)
nash_equilibrium_player2 = find_nash_equilibrium(payoff_matrix_player2)

print("Equilibrio de Nash para el jugador 1:", nash_equilibrium_player1)
print("Equilibrio de Nash para el jugador 2:", nash_equilibrium_player2)