import re

# Texto de ejemplo
text = """
El Dr. Juan Pérez es un reconocido médico en la ciudad.
María García es abogada y trabaja en un bufete de abogados.
Pedro Sánchez, ingeniero de profesión, ha sido contratado por una empresa de tecnología.
"""

# Patrones de expresiones regulares para nombres y ocupaciones
name_pattern = r"([A-Z][a-z]+(?: [A-Z][a-z]+)*)"
occupation_pattern = r"(?:es|de profesión|trabaja como) (\b\w+\b)"

# Extraer nombres y ocupaciones utilizando expresiones regulares
names = re.findall(name_pattern, text)
occupations = re.findall(occupation_pattern, text)

# Mostrar los resultados
print("Nombres encontrados:", names)
print("Ocupaciones encontradas:", occupations)