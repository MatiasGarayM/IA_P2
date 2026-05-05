from collections import deque
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbor):
        if node not in self.graph:
            self.graph[node] = []
        self.graph[node].append(neighbor)

def bfs_graph(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        node = queue.popleft()
        print(node)
        for neighbor in graph.graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

# Ejemplo de uso
g = Graph()
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')
g.add_edge('B', 'E')
g.add_edge('C', 'F')
g.add_edge('D', 'A')
g.add_edge('E', 'F')
g.add_edge('F', 'F')

print("Búsqueda en Grafos:")
bfs_graph(g, 'A')

#En este programa se separan los nodos y aristas respectivamente, por ejemplo (A,B) y luego (A,C)
#Esto significa que a pesar de estar separados los valores, B y C pertenecen al nodo A
