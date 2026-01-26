from language_model import bigram_probability


def correct_word_order(words, unigram, bigram):
    if len(words) < 2:
        return words

    for i in range(len(words) - 1):
        p1 = bigram_probability(words[i], words[i + 1], unigram, bigram)
        p2 = bigram_probability(words[i + 1], words[i], unigram, bigram)

        if p2 > p1:
            words[i], words[i + 1] = words[i + 1], words[i]

    return words


def simple_grammar_rules(words):
    corrected = []
    for i in range(len(words)):
        if words[i] == "a" and i + 1 < len(words):
            if words[i + 1][0] in "aeiou":
                corrected.append("an")
            else:
                corrected.append("a")
        else:
            corrected.append(words[i])
    return corrected
