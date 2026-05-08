import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.svm import SVC

# Cargar el conjunto de datos Iris
iris = load_iris()
X = iris.data[:, :2]  # Tomar solo las primeras dos características para la visualización
y = iris.target

# Entrenar un SVM lineal en los datos
svm = SVC(kernel='linear')
svm.fit(X, y)

# Función para visualizar la separabilidad lineal
def visualizar_separabilidad_lineal(X, y, svm_model):
    plt.figure(figsize=(8, 6))
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap='viridis', edgecolors='k', label='Datos')
    
    # Obtener los vectores de soporte y trazar la línea de separación
    plt.scatter(svm_model.support_vectors_[:, 0], svm_model.support_vectors_[:, 1], s=100, facecolors='none', edgecolors='k', label='Vectores de Soporte')
    w = svm_model.coef_[0]
    a = -w[0] / w[1]
    xx = np.linspace(X[:, 0].min() - 1, X[:, 0].max() + 1)
    yy = a * xx - (svm_model.intercept_[0]) / w[1]
    plt.plot(xx, yy, 'k-', label='Línea de Separación')

    plt.title('Separabilidad Lineal con SVM')
    plt.xlabel('Característica 1')
    plt.ylabel('Característica 2')
    plt.legend()
    plt.show()

# Visualizar la separabilidad lineal
visualizar_separabilidad_lineal(X, y, svm)