import os
#Se importa un grafo
grafo = {
	'a': [('p',4), ('j',15), ('b',1)],
    'b': [('a',1), ('d',2), ('e',2), ('c',3)],
	'j': [('a',15)],
	'p': [('a', 4)],
	'd': [('b',2), ('g',3)],
	'e': [('b',2), ('g',4), ('f',5), ('c',2)],
	'c': [('b',3), ('e',2), ('f',5), ('i',20)],
	'g': [('d',3), ('e',4), ('f',10), ('h',1)],
	'f': [('g',10), ('e',5), ('c',5)],
	'i': [('c',20)],
	'h': [('g',1)] 
}

#Imprime el grafo 
print("Muestra el grafo antes del recorrido: \n")
for key, lista in grafo.items():
	print(key)
	print(lista)
print()
		
visitados = [] #Lista de objetos ya revisados
pila = [] #Lista de objetos por revisar pero hacia al fondo

origen = input("Ingresa un nodo: ") #Se ingresa el nodo con el que empezar
print("\nLista de recorrido en profundidad\n")
pila.append(origen) # Se coloca el vertice en el origen de la pila

while pila: #Mientras la pila no este vacia, entonces: 
	actual = pila.pop() #Se selecciona el vertice y lo manda como el actual

	if actual not in visitados: #Si el vertice actual no se ha visitado
		print("Vertice actual -> ", actual) #Imprime el vertice
		visitados.append(actual) #Guarda el vertice en la lista de visitados

	for key, lista in grafo[actual]: #Cada vertice que tiene de destino no visitado
		if key not in visitados:
			pila.append(key) #Pone el vertice en la lista de no visitados

print()
os.system("pause")

#Este a diferencia de la busqueda por anchura, selecciona el ultimo valor de cada nodo y lo coloca como el actual
#Llendo al final de la lista antes de seguir buscando vertices en cualquier punto
#En otras palabras: Selecciona el ultimo, busca el ultimo EN el ultimo y asi hasta llegar al fondo