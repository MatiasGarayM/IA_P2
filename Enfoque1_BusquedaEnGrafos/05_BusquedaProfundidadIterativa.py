def dls(graph, start, depth, visited=None):
    if visited is None:
        visited = set()
    if depth >= 0:
        visited.add(start)
        print(start)
        for neighbor in graph[start]:
            if neighbor not in visited:
                dls(graph, neighbor, depth - 1, visited)

def ids(graph, start, max_depth):
    for depth in range(max_depth):
        print(f"Depth Limit: {depth}")
        dls(graph, start, depth)

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("Búsqueda en Profundidad Iterativa:")
ids(graph, 'A', 3)

#Este, a diferencia de la busqueda limitada, diferencia todos y cada uno de los niveles en los que busca
#Si yo selecciono 2, Detecta el nodo A (limite 0) y luego busca dentro de A (limite 1), separando las busquedas individualmente
#En cambio si yo pongo 3, Detecta A, Busca dentro de A (B y C), y por ultimo, busca dentro de B y C, igualmente, separando las busquedas