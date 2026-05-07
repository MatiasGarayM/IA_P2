# Calculamos el valor de la información
def information_value(probability, utility_with_info, utility_without_info):
    return probability * utility_with_info + (1 - probability) * utility_without_info

# Ejemplo de uso
probability = 0.8
utility_with_info = 100
utility_without_info = 50
value = information_value(probability, utility_with_info, utility_without_info)
print(f"El valor de la información es: {value}")