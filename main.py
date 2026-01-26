from correcteur import *

# Charger et préparer le corpus
texte = charger_corpus("corpus.txt")
tokens = tokenizer(texte)
freq = frequences(tokens)
vocabulaire = freq.keys()

# Phrase à corriger
# phrase = "le traitemant automatiqe des langes"
phrase = "ce projt utilise un modle biramme simple"

print("Phrase originale :", phrase)
print("Phrase corrigée  :", corriger_phrase(phrase, vocabulaire))
