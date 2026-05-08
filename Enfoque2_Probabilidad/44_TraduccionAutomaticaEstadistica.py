import numpy as np

# Función para entrenar el modelo IBM Model 1
def train_ibm_model1(source_corpus, target_corpus, num_iterations=10):
    source_vocab = set(word for sentence in source_corpus for word in sentence)
    target_vocab = set(word for sentence in target_corpus for word in sentence)
    source_vocab_size = len(source_vocab)
    target_vocab_size = len(target_vocab)
    alignment_probs = np.ones((target_vocab_size, source_vocab_size)) / source_vocab_size

    for _ in range(num_iterations):
        count = np.zeros((target_vocab_size, source_vocab_size))
        total = np.zeros(target_vocab_size)

        for source_sentence, target_sentence in zip(source_corpus, target_corpus):
            for target_word in target_sentence:
                total_s = 0
                for source_word in source_sentence:
                    total_s += alignment_probs[target_vocab.index(target_word), source_vocab.index(source_word)]
                for source_word in source_sentence:
                    count[target_vocab.index(target_word), source_vocab.index(source_word)] += alignment_probs[target_vocab.index(target_word), source_vocab.index(source_word)] / total_s
                    total[target_vocab.index(target_word)] += alignment_probs[target_vocab.index(target_word), source_vocab.index(source_word)] / total_s

        for target_word in target_vocab:
            for source_word in source_vocab:
                alignment_probs[target_vocab.index(target_word), source_vocab.index(source_word)] = count[target_vocab.index(target_word), source_vocab.index(source_word)] / total[target_vocab.index(target_word)]

    return alignment_probs

# Ejemplo de uso
source_corpus = [['la', 'casa', 'es', 'grande'], ['el', 'perro', 'come', 'comida']]
target_corpus = [['the', 'house', 'is', 'big'], ['the', 'dog', 'eats', 'food']]

alignment_probs = train_ibm_model1(source_corpus, target_corpus)

# Mostrar la matriz de probabilidades de alineación
print("Matriz de probabilidades de alineación (IBM Model 1):")
print(alignment_probs)