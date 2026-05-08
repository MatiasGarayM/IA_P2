import matplotlib.pyplot as plt
import numpy as np

# Generar datos
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Graficar
plt.plot(x, y)
plt.title('Gráfico por Computador: Función Seno')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.grid(True)
plt.show()