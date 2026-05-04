def dls(graph, start, depth, visited=None):
    if visited is None:
        visited = set()
    if depth >= 0:
        visited.add(start)
        print(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dls(graph, neighbor, depth - 1, visited)

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("Búsqueda en Profundidad Limitada:")
dls(graph, 'A', 2)

#Aqui, se coloca un límite numerico para que la busqueda se detenga funcionando de la siguiente manera:
#1: Busca en el primer nivel, 2: Busca en el primer nivel y en sus hijos (por ejemplo, se busca en A y luego, dentro de C y B)
#3: Busca en A, luego busca dentro de C y B, y por ultimo busca dentro de F (que esta en C) y en E y D (que esta dentro de B)
#Y así sucesivamente