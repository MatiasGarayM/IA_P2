# Probabilidad a priori de tener una enfermedad
probabilidad_enfermedad = 0.01

# Sensibilidad de la prueba (probabilidad de que la prueba sea positiva dado que tienes la enfermedad)
sensibilidad_prueba = 0.95

# Especificidad de la prueba (probabilidad de que la prueba sea negativa dado que no tienes la enfermedad)
especificidad_prueba = 0.90

# Calcular la probabilidad de tener la enfermedad dado que la prueba es positiva usando la regla de Bayes
probabilidad_positiva_dado_enfermedad = sensibilidad_prueba
probabilidad_positiva_dado_no_enfermedad = 1 - especificidad_prueba
probabilidad_enfermedad_dado_positiva = (probabilidad_positiva_dado_enfermedad * probabilidad_enfermedad) / ((probabilidad_positiva_dado_enfermedad * probabilidad_enfermedad) + (probabilidad_positiva_dado_no_enfermedad * (1 - probabilidad_enfermedad)))

print("Probabilidad de tener la enfermedad dado que la prueba es positiva:", probabilidad_enfermedad_dado_positiva)