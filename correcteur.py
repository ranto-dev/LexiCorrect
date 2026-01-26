# ===============================
# Chargement du corpus
# ===============================

def charger_corpus(fichier):
    with open(fichier, "r", encoding="utf-8") as f:
        texte = f.read().lower()
    return texte


def tokenizer(texte):
    mots = ""
    tokens = []
    for c in texte:
        if c.isalpha() or c == " ":
            mots += c
    for mot in mots.split():
        tokens.append(mot)
    return tokens


def frequences(tokens):
    freq = {}
    for mot in tokens:
        freq[mot] = freq.get(mot, 0) + 1
    return freq


# ===============================
# Distance de Levenshtein
# ===============================

def distance_edition(m1, m2):
    dp = [[0 for _ in range(len(m2) + 1)] for _ in range(len(m1) + 1)]

    for i in range(len(m1) + 1):
        dp[i][0] = i
    for j in range(len(m2) + 1):
        dp[0][j] = j

    for i in range(1, len(m1) + 1):
        for j in range(1, len(m2) + 1):
            cout = 0 if m1[i - 1] == m2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,      # suppression
                dp[i][j - 1] + 1,      # insertion
                dp[i - 1][j - 1] + cout  # substitution
            )

    return dp[-1][-1]


# ===============================
# Correction orthographique
# ===============================

def corriger_mot(mot, vocabulaire):
    if mot in vocabulaire:
        return mot

    meilleur = mot
    distance_min = float("inf")

    for v in vocabulaire:
        d = distance_edition(mot, v)
        if d < distance_min:
            distance_min = d
            meilleur = v

    return meilleur


def corriger_phrase(phrase, vocabulaire):
    phrase = phrase.lower()
    mots = phrase.split()
    phrase_corrigee = []

    for mot in mots:
        mot_corrige = corriger_mot(mot, vocabulaire)
        phrase_corrigee.append(mot_corrige)

    return " ".join(phrase_corrigee)
