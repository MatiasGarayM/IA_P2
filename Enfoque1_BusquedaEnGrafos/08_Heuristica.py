def euclidean_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2) ** 0.5

# Ejemplo de uso
point_A = (1, 2)
point_B = (4, 6)
distance = euclidean_distance(point_A, point_B)
print("Distancia Euclidiana:", distance)

#Este programa calcula la distancia Euclidiana en un espacio bidimensional
#Este valor nos sirve para metodos de busqueda informada como A*