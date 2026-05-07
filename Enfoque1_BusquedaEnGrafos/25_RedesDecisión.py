import pydot

# Creamos un gráfico de red de decisión
graph = pydot.Dot(graph_type='digraph')

# Agregamos nodos
node_a = pydot.Node("A", label="Tomar Café")
node_b = pydot.Node("B", label="Estudiar")
node_c = pydot.Node("C", label="Salir con Amigos")

graph.add_node(node_a)
graph.add_node(node_b)
graph.add_node(node_c)

# Agregamos arcos (transiciones)
graph.add_edge(pydot.Edge(node_a, node_b, label="Cansado"))
graph.add_edge(pydot.Edge(node_a, node_c, label="Despierto"))

# Guardamos el gráfico
graph.write_png('decision_tree.png')