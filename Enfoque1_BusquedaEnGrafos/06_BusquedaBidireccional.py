from collections import deque

def bidirectional_search(graph, start, goal):
    forward_visited = set()
    backward_visited = set()
    forward_queue = deque([start])
    backward_queue = deque([goal])
    forward_visited.add(start)
    backward_visited.add(goal)

    while forward_queue and backward_queue:
        # Expandir desde el lado forward
        current_forward = forward_queue.popleft()
        print("Forward:", current_forward)
        if current_forward in backward_visited:
            print("Goal reached!")
            return
        for neighbor in graph[current_forward]:
            if neighbor not in forward_visited:
                forward_queue.append(neighbor)
                forward_visited.add(neighbor)

        # Expandir desde el lado backward
        current_backward = backward_queue.popleft()
        print("Backward:", current_backward)
        if current_backward in forward_visited:
            print("Goal reached!")
            return
        for neighbor in graph[current_backward]:
            if neighbor not in backward_visited:
                backward_queue.append(neighbor)
                backward_visited.add(neighbor)

# Ejemplo de uso
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F', 'A'],
    'F': []
}
print("Búsqueda Bidireccional:")
bidirectional_search(graph, 'A', 'E')

#Este programa busca desde dos nodos diferentes, empieza con el principal (nodo A) y sigue con el secundario (nodo E)
#El objetivo como tal es que los dos nodos de busqueda se encuentren, intercalando la busqueda uno a uno hasta llegar a la meta