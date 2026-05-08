# Lista de documentos
documents = [
    "El cielo es azul.",
    "El sol brilla en el cielo.",
    "Las nubes cubren el cielo.",
    "El perro corre por el parque.",
    "Los pájaros cantan en los árboles."
]

# Función de recuperación de datos
def retrieve_documents(query, documents):
    results = []
    for doc in documents:
        if query.lower() in doc.lower():
            results.append(doc)
    return results

# Realizar una búsqueda por palabra clave
query = "cielo"
results = retrieve_documents(query, documents)

# Mostrar los resultados
print("Documentos que contienen la palabra clave '{}':".format(query))
for idx, result in enumerate(results, start=1):
    print("Documento {}: {}".format(idx, result))