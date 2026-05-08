import numpy as np
import pymc3 as pm

# Datos observados
datos = np.random.normal(loc=5, scale=2, size=100)

# Definir el modelo bayesiano
with pm.Model() as modelo:
    # Parámetros priors
    media = pm.Normal('media', mu=0, sigma=10)
    sigma = pm.HalfNormal('sigma', sigma=10)

    # Likelihood
    observaciones = pm.Normal('observaciones', mu=media, sigma=sigma, observed=datos)

    # Realizar muestreo MCMC
    traza = pm.sample(1000, tune=1000)

# Analizar resultados
print(pm.summary(traza))