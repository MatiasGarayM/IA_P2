import numpy as np
import pymc3 as pm

# Definir la matriz de transición
prob_transicion = np.array([[0.9, 0.1], [0.3, 0.7]])

# Definir el modelo de Manto de Markov
with pm.Model() as modelo_manto:
    # Definir estado inicial uniformemente aleatorio
    estado_inicial = pm.Categorical('estado_inicial', p=np.array([0.5, 0.5]))
    
    # Definir matriz de transición como variable determinista
    matriz_transicion = pm.Deterministic('matriz_transicion', prob_transicion)
    
    # Generar secuencia de observaciones
    secuencia_observaciones = pm.MarkovChain('secuencia_observaciones', p=matriz_transicion, 
                                             shape=100)

    # Muestreo MCMC
    traza = pm.sample(1000, tune=1000)

# Imprimir resumen de la traza
print(pm.summary(traza))