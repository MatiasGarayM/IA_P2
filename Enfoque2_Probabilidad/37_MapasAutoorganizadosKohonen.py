import numpy as np
import matplotlib.pyplot as plt
from minisom import MiniSom
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos Iris
iris = load_iris()
X, y = iris.data, iris.target

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Crear el mapa autoorganizado de Kohonen
som = MiniSom(7, 7, X.shape[1], sigma=0.3, learning_rate=0.5)
som.random_weights_init(X_scaled)
som.train_random(X_scaled, 1000)

# Visualizar los resultados en el mapa
plt.figure(figsize=(8, 6))
plt.pcolor(som.distance_map().T, cmap='bone_r')  # distancias de los pesos
plt.colorbar()

# Asignar colores a las clases y mostrar los puntos en el mapa
markers = ['o', 's', 'D']
colors = ['r', 'g', 'b']
for i, x in enumerate(X_scaled):
    w = som.winner(x)
    plt.plot(w[0] + 0.5, w[1] + 0.5, markers[y[i]], markerfacecolor='None', markeredgecolor=colors[y[i]], markersize=10, markeredgewidth=2)

plt.title('Mapa Autoorganizado de Kohonen')
plt.show()