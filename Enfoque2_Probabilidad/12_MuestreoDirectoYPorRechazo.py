from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.sampling import BayesianModelSampling

# Definir la estructura de la red bayesiana
modelo = BayesianNetwork([('A', 'B'), ('A', 'C')])

# Definir las distribuciones de probabilidad condicional (CPD)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.2], [0.8]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.3, 0.7], [0.8, 0.2]],
                   evidence=['A'], evidence_card=[2])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.4, 0.6], [0.7, 0.3]],
                   evidence=['A'], evidence_card=[2])

# Asociar CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C)

# Realizar muestreo directo
muestreo_directo = BayesianModelSampling(modelo)
muestra_directa = muestreo_directo.forward_sample(size=1000)

# Realizar muestreo por rechazo
muestreo_rechazo = BayesianModelSampling(modelo)
muestra_rechazo = muestreo_rechazo.rejection_sample(evidence=None, size=1000)

print("Muestreo Directo:")
print(muestra_directa)
print("\nMuestreo por Rechazo:")
print(muestra_rechazo)