from keyboard_model import KEYBOARD_CONFUSION


def edit_distance(w1, w2):
    dp = [[0] * (len(w2) + 1) for _ in range(len(w1) + 1)]

    for i in range(len(w1) + 1):
        dp[i][0] = i
    for j in range(len(w2) + 1):
        dp[0][j] = j

    for i in range(1, len(w1) + 1):
        for j in range(1, len(w2) + 1):
            cost = 0 if w1[i - 1] == w2[j - 1] else 1
            dp[i][j] = min(
                dp[i - 1][j] + 1,
                dp[i][j - 1] + 1,
                dp[i - 1][j - 1] + cost
            )

    return dp[-1][-1]


def keyboard_penalty(w1, w2):
    penalty = 0
    for i in range(min(len(w1), len(w2))):
        if w1[i] != w2[i]:
            if w1[i] in KEYBOARD_CONFUSION and w2[i] in KEYBOARD_CONFUSION[w1[i]]:
                penalty -= 0.5
            else:
                penalty += 1
    return penalty


def correct_word(word, vocabulary, unigram):
    if word in vocabulary:
        return word

    best_word = word
    best_score = float("-inf")

    for v in vocabulary:
        score = (
            -edit_distance(word, v)
            + unigram.get(v, 1)
            - keyboard_penalty(word, v)
        )
        if score > best_score:
            best_score = score
            best_word = v

    return best_word
