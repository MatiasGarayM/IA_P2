import numpy as np
from sklearn.datasets import make_blobs
from sklearn.mixture import GaussianMixture

# Generar datos de muestra
X, _ = make_blobs(n_samples=1000, centers=3, random_state=42)

# Inicializar y ajustar el modelo de mezcla gaussiana
gmm = GaussianMixture(n_components=3, random_state=42)
gmm.fit(X)

# Mostrar los parámetros estimados
print("Parámetros de las componentes del modelo:")
for i in range(gmm.n_components):
    print(f"Componente {i+1}:")
    print("Media:", gmm.means_[i])
    print("Covarianza:", gmm.covariances_[i])
    print()

# Mostrar las etiquetas predichas
y_pred = gmm.predict(X)
print("Etiquetas predichas:")
print(y_pred)