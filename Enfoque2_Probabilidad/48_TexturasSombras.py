import matplotlib.pyplot as plt
import numpy as np

# Generar una matriz de ruido aleatorio para simular una textura
texture = np.random.rand(100, 100)

# Crear un degradado lineal para simular una fuente de luz
gradient = np.linspace(0, 1, 100)

# Calcular la sombra utilizando la matriz de textura y el degradado lineal
shadow = texture * gradient[:, np.newaxis]

# Graficar la textura y la sombra
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(texture, cmap='gray')
plt.title('Textura')

plt.subplot(1, 2, 2)
plt.imshow(shadow, cmap='gray')
plt.title('Sombra')

plt.show()