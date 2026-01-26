def load_corpus(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().lower()


def tokenize(text):
    clean = ""
    for c in text:
        if c.isalpha() or c == " ":
            clean += c
    return clean.split()


def build_unigram(tokens):
    model = {}
    for word in tokens:
        model[word] = model.get(word, 0) + 1
    return model


def build_bigram(tokens):
    model = {}
    for i in range(len(tokens) - 1):
        pair = (tokens[i], tokens[i + 1])
        model[pair] = model.get(pair, 0) + 1
    return model


def bigram_probability(w1, w2, unigram, bigram):
    if (w1, w2) in bigram and w1 in unigram:
        return bigram[(w1, w2)] / unigram[w1]
    return 0.000001
