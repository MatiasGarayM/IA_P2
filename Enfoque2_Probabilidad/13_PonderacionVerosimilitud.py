from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import Importance

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

# Realizar ponderación de verosimilitud en el modelo
inferencia = Importance(modelo)
probabilidad_B_C_dado_A_0 = inferencia.likelihood_weighted_sample(evidence={'A': 0}, size=1000)

print("Probabilidad estimada de P(B, C | A=0) mediante ponderación de verosimilitud:")
print(probabilidad_B_C_dado_A_0)