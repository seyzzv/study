def solution(n, words):
    used = set()
    for i, word in enumerate(words):
        if word in used:
            return [(i % n) + 1, (i // n) + 1]
        if i > 0 and words[i-1][-1] != word[0]:
            return [(i % n) + 1, (i // n) + 1]
        used.add(word)
    return [0, 0]