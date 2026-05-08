import numpy as np
from hmmlearn import hmm

# Definir el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2)

# Matriz de transición
modelo_hmm.transmat_ = np.array([[0.7, 0.3], [0.4, 0.6]])

# Probabilidades iniciales de los estados
modelo_hmm.startprob_ = np.array([0.5, 0.5])

# Matriz de emisión
modelo_hmm.emissionprob_ = np.array([[0.1, 0.4, 0.5], [0.6, 0.3, 0.1]])

# Secuencia de observaciones
observaciones = np.array([[0], [1], [0], [2]])

# Decodificar la secuencia de observaciones utilizando el algoritmo de Viterbi
secuencia_estados = modelo_hmm.predict(observaciones)

print("Secuencia de Estados Decodificada:", secuencia_estados)