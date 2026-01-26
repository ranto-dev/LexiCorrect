from language_model import *
from spell_corrector import *
from grammar_corrector import *

text = load_corpus("corpus.txt")
tokens = tokenize(text)

unigram = build_unigram(tokens)
bigram = build_bigram(tokens)
vocabulary = unigram.keys()

sentence = "le traitemant automtique des langes est importent"

words = sentence.lower().split()

# Spell correction
corrected_words = [correct_word(w, vocabulary, unigram) for w in words]

# Word order correction
corrected_words = correct_word_order(corrected_words, unigram, bigram)

# Grammar correction
corrected_words = simple_grammar_rules(corrected_words)

print("Original sentence :", sentence)
print("Corrected sentence:", " ".join(corrected_words))
