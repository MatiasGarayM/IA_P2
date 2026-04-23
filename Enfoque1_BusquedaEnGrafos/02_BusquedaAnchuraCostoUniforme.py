import heapq
import networkx as nx

# 1. Definición de los datos (Lo que antes intentabas importar)
MODO    = "pesos"
INICIO  = "A"
DESTINO = "F"

GRAFO = {
    "A": [("B", 2.0), ("C", 3.0)],
    "B": [("A", 2.0), ("D", 4.0), ("E", 1.0)],
    "C": [("A", 3.0), ("F", 2.0)],
    "D": [("B", 4.0), ("F", 5.0)],
    "E": [("B", 1.0)],
    "F": [("C", 2.0), ("D", 5.0)],
}

print(f"Grafo cargado: {GRAFO}  Inicio: {INICIO}  |  Destino: {DESTINO}")

# 2. Algoritmo Uniform Cost Search (UCS)
def ucs(grafo, inicio, destino):
    # La cola de prioridad guarda tuplas: (costo_acumulado, [camino_recorrido])
    cola = [(0, [inicio])]
    visitado = set()

    while cola:
        costo, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo in visitado:
            continue
        
        visitado.add(nodo)

        # Si llegamos al objetivo, terminamos
        if nodo == destino:
            print(f"Costo total acumulado: {costo}")
            return camino

        # Explorar vecinos
        for vecino, peso in grafo.get(nodo, []):
            if vecino not in visitado:
                nuevo_costo = costo + peso
                # Se suma el camino actual con el nuevo vecino
                heapq.heappush(cola, (nuevo_costo, camino + [vecino]))

    return None

# 3. Ejecución
camino_optimo = ucs(GRAFO, INICIO, DESTINO)

if camino_optimo:
    print("El camino más barato es:", " -> ".join(camino_optimo))
else:
    print("No se encontró camino.")