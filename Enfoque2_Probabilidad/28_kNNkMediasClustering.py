import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans

# Generar datos de muestra
X, y = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Inicializar y ajustar el clasificador k-NN
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)

# Inicializar y ajustar el modelo k-Medias
kmeans = KMeans(n_clusters=4)
kmeans.fit(X)

# Visualizar los clústeres y los límites de decisión del clasificador k-NN
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis')
plt.title('Clústeres Verdaderos')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

plt.subplot(1, 2, 2)
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], marker='o', c='red', s=200, alpha=0.9)
plt.title('Clústeres Predichos por k-Medias')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')

plt.show()