import numpy as np
import pymc3 as pm

# Definir probabilidades de transición
prob_transicion = np.array([[0.9, 0.1],   # Probabilidad de mantenerse en el mismo estado o cambiar
                             [0.2, 0.8]]) # Probabilidad de cambiar de estado o mantenerse

# Generar secuencia de observaciones
np.random.seed(0)  # Semilla para reproducibilidad
n_observaciones = 100
observaciones = np.zeros(n_observaciones, dtype=int)

estado_actual = 0  # Empezar en el estado 0
for i in range(n_observaciones):
    observaciones[i] = estado_actual
    estado_actual = np.random.choice([0, 1], p=prob_transicion[estado_actual])

# Definir el modelo de Manto de Markov
with pm.Model() as modelo_manto:
    # Definir matriz de transición como variable determinista
    matriz_transicion = pm.Deterministic('matriz_transicion', prob_transicion)
    
    # Definir estado inicial uniformemente aleatorio
    estado_inicial = pm.Categorical('estado_inicial', p=np.array([0.5, 0.5]))
    
    # Generar secuencia de observaciones
    secuencia_observaciones = pm.MarkovChain('secuencia_observaciones', p=matriz_transicion, 
                                             shape=n_observaciones, observed=observaciones)
    
    # Muestreo MCMC
    traza = pm.sample(1000, tune=1000)

# Imprimir resumen de la traza
print(pm.summary(traza))