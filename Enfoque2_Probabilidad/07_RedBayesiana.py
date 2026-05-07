from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

# Definir la estructura de la red bayesiana
modelo = BayesianNetwork([('A', 'C'), ('B', 'C')])

# Definir las distribuciones de probabilidad condicional (CPD)
cpd_A = TabularCPD(variable='A', variable_card=2, values=[[0.6], [0.4]])
cpd_B = TabularCPD(variable='B', variable_card=2, values=[[0.7], [0.3]])
cpd_C = TabularCPD(variable='C', variable_card=2, values=[[0.9, 0.6, 0.7, 0.1], [0.1, 0.4, 0.3, 0.9]],
                   evidence=['A', 'B'], evidence_card=[2, 2])

# Asociar CPDs al modelo
modelo.add_cpds(cpd_A, cpd_B, cpd_C)

# Verificar la validez del modelo
print("¿El modelo es válido?", modelo.check_model())