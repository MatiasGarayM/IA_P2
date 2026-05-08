import numpy as np

# Función de activación Sigmoide
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Función de activación ReLU (Rectified Linear Unit)
def relu(x):
    return np.maximum(0, x)

# Función de activación Tangente Hiperbólica
def tanh(x):
    return np.tanh(x)

# Función de activación Softmax (para problemas de clasificación multiclase)
def softmax(x):
    exp_scores = np.exp(x)
    return exp_scores / np.sum(exp_scores, axis=1, keepdims=True)

# Ejemplo de uso de las funciones de activación
entrada = np.array([1, 2, 3])

# Aplicar las funciones de activación a la entrada
print("Sigmoide:", sigmoide(entrada))
print("ReLU:", relu(entrada))
print("Tangente Hiperbólica:", tanh(entrada))

# Para la función Softmax, la entrada debe ser una matriz de scores
scores = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("Softmax:", softmax(scores))