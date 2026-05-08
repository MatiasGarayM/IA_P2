import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

# Generar datos de muestra
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Inicializar y ajustar el modelo de k-Means
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)

# Obtener las etiquetas de los clústeres y los centros de los clústeres
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# Visualizar los clústeres y los centros
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], marker='o', c='red', s=200, alpha=0.9)
plt.title('Clústeres y Centros de k-Means')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()