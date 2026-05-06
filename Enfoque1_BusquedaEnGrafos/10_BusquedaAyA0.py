def astar_search(graph, start, goal, heuristic):
    open_list = [(heuristic(start), start)]  # Lista de nodos a explorar, con prioridad según la heurística
    closed_list = set()  # Conjunto de nodos explorados
    while open_list:
        _, current = open_list.pop(0)  # Sacamos el nodo con menor f = g + h
        if current == goal:
            print("¡Objetivo alcanzado!")
            return
        if current not in closed_list:
            print("Visitando:", current)
            closed_list.add(current)
            for neighbor in graph[current]:
                if neighbor not in closed_list:
                    open_list.append((heuristic(neighbor), neighbor))
            open_list.sort(key=lambda x: x[0])  # Ordenamos la lista según la heurística

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
heuristic = {'A': 5, 'B': 3, 'C': 2, 'D': 4, 'E': 2, 'F': 0}
print("Búsqueda A*:")
astar_search(graph, 'A', 'E', heuristic.get)

#Este, a diferencia de la busqueda voraz, Busca en todos los nodos para encontrar de alguna manera
#el camino mas corto hacia el nodo destino, esto significa que analiza las posibilidades antes de
#buscar el camino mas corto hacia el destino, estima la distancia de un punto a otro y luego realiza la acción