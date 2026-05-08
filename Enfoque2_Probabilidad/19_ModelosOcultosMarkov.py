from hmmlearn import hmm

# Definir y entrenar el modelo HMM
modelo_hmm = hmm.MultinomialHMM(n_components=2)
observaciones = [[0], [1], [0], [2]]  # Secuencia de observaciones
longitudes_secuencia = [len(observaciones)]
modelo_hmm.fit(observaciones, longitudes_secuencia)

# Predecir la secuencia de estados ocultos
secuencia_estados = modelo_hmm.predict(observaciones)

print("Secuencia de Estados Ocultos Predicha:", secuencia_estados)