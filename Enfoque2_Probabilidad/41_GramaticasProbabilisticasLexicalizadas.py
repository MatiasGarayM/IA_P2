import nltk

# Descargar recursos necesarios de NLTK
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Definir una oración de ejemplo
sentence = "The quick brown fox jumps over the lazy dog."

# Tokenizar la oración y etiquetar las palabras con POS tags
tokens = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(tokens)

# Entrenar un parser lexicalizado PCFG
from nltk.parse import pchart
from nltk.corpus import treebank
pcfg_grammar = nltk.PCFG.fromstring("""
    S -> NP VP [1.0]
    NP -> DT N [0.7] | NP PP [0.3]
    VP -> V NP [0.5] | V [0.5]
    PP -> P NP [1.0]
    DT -> 'the' [0.5] | 'a' [0.5]
    N -> 'fox' [0.4] | 'dog' [0.3] | 'cat' [0.3]
    V -> 'jumps' [0.6] | 'runs' [0.4]
    P -> 'over' [1.0]
""")

# Crear un parser lexicalizado basado en la PCFG
parser = pchart.InsideChartParser(pcfg_grammar)

# Analizar sintácticamente la oración
for parse in parser.parse(tokens):
    print(parse)
    parse.draw()  # Dibujar el árbol sintáctico
    break  # Detenerse después de encontrar la primera analisis válido