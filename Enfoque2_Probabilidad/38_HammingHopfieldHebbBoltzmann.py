import numpy as np
from scipy.special import expit

'''
# Red Neuronal de Hamming
'''
class HammingNetwork:
    def __init__(self, pattern_size):
        self.weights = np.zeros((pattern_size, pattern_size))

    def train(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)

    def predict(self, pattern):
        return np.sign(np.dot(pattern, self.weights))

# Ejemplo de uso de la red de Hamming
pattern_size = 4
patterns = np.array([[1, -1, 1, -1], [-1, -1, 1, 1]])
hamming_net = HammingNetwork(pattern_size)
hamming_net.train(patterns)
test_pattern = np.array([1, -1, 1, 1])
print("Resultado de la predicción de la red de Hamming:", hamming_net.predict(test_pattern))


'''
# Red Neuronal de Hopfield
'''
class HopfieldNetwork:
    def __init__(self, pattern_size):
        self.weights = np.zeros((pattern_size, pattern_size))

    def train(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)

    def predict(self, pattern):
        for _ in range(100):
            pattern = expit(np.dot(self.weights, pattern))
        return np.sign(pattern)

# Ejemplo de uso de la red de Hopfield
hopfield_net = HopfieldNetwork(pattern_size)
hopfield_net.train(patterns)
print("Resultado de la predicción de la red de Hopfield:", hopfield_net.predict(test_pattern))


'''
# Regla de Aprendizaje de Hebb
'''
class HebbRule:
    def __init__(self, input_size):
        self.weights = np.zeros((input_size, input_size))

    def train(self, patterns):
        for pattern in patterns:
            self.weights += np.outer(pattern, pattern)

    def predict(self, pattern):
        return np.sign(np.dot(pattern, self.weights))

# Ejemplo de uso de la regla de aprendizaje de Hebb
hebb_rule = HebbRule(pattern_size)
hebb_rule.train(patterns)
print("Resultado de la predicción utilizando la regla de aprendizaje de Hebb:", hebb_rule.predict(test_pattern))


'''
# Máquina de Boltzmann
'''
class BoltzmannMachine:
    def __init__(self, num_units):
        self.num_units = num_units
        self.weights = np.random.randn(num_units, num_units)

    def train(self, data, epochs):
        for _ in range(epochs):
            for sample in data:
                for _ in range(100):
                    idx = np.random.randint(self.num_units)
                    activation = expit(np.dot(self.weights[idx], sample))
                    sample[idx] = np.random.choice([-1, 1], p=[1-activation, activation])
                self.weights += np.outer(sample, sample)

    def predict(self, data):
        predictions = []
        for sample in data:
            for _ in range(100):
                idx = np.random.randint(self.num_units)
                activation = expit(np.dot(self.weights[idx], sample))
                sample[idx] = np.random.choice([-1, 1], p=[1-activation, activation])
            predictions.append(sample)
        return predictions

# Ejemplo de uso de la Máquina de Boltzmann
data = np.array([[1, -1, 1, -1], [-1, -1, 1, 1]])
boltzmann_machine = BoltzmannMachine(pattern_size)
boltzmann_machine.train(data, epochs=100)
print("Resultados de la predicción utilizando la Máquina de Boltzmann:", boltzmann_machine.predict(data))