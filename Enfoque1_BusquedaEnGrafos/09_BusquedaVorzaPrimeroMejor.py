def greedy_best_first_search(graph, start, goal, heuristic):
    visited = set()
    priority_queue = [(heuristic(start), start)]  # Cola de prioridad según la heurística
    while priority_queue:
        _, current = priority_queue.pop(0)  # Sacamos el elemento de menor costo según la heurística
        if current == goal:
            print("¡Objetivo alcanzado!")
            return
        if current not in visited:
            print("Visitando:", current)
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    priority_queue.append((heuristic(neighbor), neighbor))
            priority_queue.sort(key=lambda x: x[0])  # Ordenamos la cola de prioridad según la heurística

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
print("Búsqueda Voraz Primero el Mejor:")
greedy_best_first_search(graph, 'A', 'E', heuristic.get)

#El objetivo de este programa es el encontrar la ruta mas corta para llegar de un nodo a otro
#Para esto se utiliza la heuristica, que calcula la distancia mas corta de una sección a otra
#Acumula las secciones mas cortas y encuentra el camino mas rápido para llegar al nodo destino