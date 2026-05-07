# Probabilidad de obtener una cara en un lanzamiento de una moneda justo
probabilidad_cara = 0.5

# Probabilidad de obtener una cara y un número par (asumiendo que la moneda es justa)
probabilidad_cara_y_par = 0.25

# Calcular la probabilidad condicionada de obtener un número par dado que se obtuvo una cara
probabilidad_par_dado_cara = probabilidad_cara_y_par / probabilidad_cara

print("Probabilidad condicionada de obtener un número par dado que se obtuvo una cara:", probabilidad_par_dado_cara)