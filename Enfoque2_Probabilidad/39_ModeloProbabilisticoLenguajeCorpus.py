import nltk
import random

# Descargar recursos necesarios de NLTK
nltk.download('punkt')

# Leer y preprocesar el corpus de texto
corpus_file = 'corpus.txt'
with open(corpus_file, 'r', encoding='utf-8') as file:
    corpus = file.read()

# Tokenizar el corpus en palabras
tokens = nltk.word_tokenize(corpus)

# Construir un modelo de bigramas
bigrams = list(nltk.bigrams(tokens))
bigram_model = nltk.ConditionalFreqDist(bigrams)

# Generar texto nuevo utilizando el modelo de bigramas
def generate_text(seed_word, length=20):
    word = seed_word
    generated_text = [word]
    for _ in range(length):
        next_word = random.choice(list(bigram_model[word].keys()))
        generated_text.append(next_word)
        word = next_word
    return ' '.join(generated_text)

# Ejemplo de uso: generar texto nuevo a partir de una semilla
seed_word = 'the'
generated_text = generate_text(seed_word)
print("Texto generado:", generated_text)