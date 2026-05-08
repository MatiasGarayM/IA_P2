import nltk

# Descargar recursos necesarios de NLTK
nltk.download('treebank')

# Cargar el corpus de Penn Treebank
from nltk.corpus import treebank
sentences = treebank.parsed_sents()

# Entrenar una PCFG a partir del corpus
from nltk import treetransforms
from nltk import induce_pcfg
productions = []
for tree in sentences:
    tree.collapse_unary(collapsePOS=True)
    tree.chomsky_normal_form(horzMarkov=2)
    productions += tree.productions()
grammar = induce_pcfg(nltk.Nonterminal('S'), productions)

# Generar oraciones sintácticamente correctas utilizando la PCFG
from nltk.parse.generate import generate
for sentence in generate(grammar, depth=5):
    print(' '.join(sentence))
    break  # Imprimir solo la primera oración para evitar un bucle infinito