import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_circles
from sklearn.svm import SVC

# Generar datos de muestra en forma de círculos concéntricos
X, y = make_circles(n_samples=100, noise=0.1, factor=0.4, random_state=42)

# Inicializar y ajustar la SVM con un kernel polinomial
svm = SVC(kernel='poly', degree=3, C=10)
svm.fit(X, y)

# Crear una malla para visualizar los límites de decisión
xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 100))
Z = svm.decision_function(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Visualizar los datos y los límites de decisión
plt.figure(figsize=(8, 6))
plt.contourf(xx, yy, Z, levels=np.linspace(Z.min(), 0, 7), cmap=plt.cm.PuBu, alpha=0.8)
plt.contour(xx, yy, Z, levels=[0], linewidths=2, colors='darkred')
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired, edgecolors='k')
plt.title('SVM con Kernel Polinomial')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.show()