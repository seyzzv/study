def solution(sticker):
    n = len(sticker)
    if n <= 2:
        return max(sticker) if sticker else 0

    p2, p1 = sticker[0], sticker[0]
    for i in range(2, n - 1):
        p2, p1 = p1, max(p1, p2 + sticker[i])
    c1 = p1

    p2, p1 = 0, sticker[1]
    for i in range(2, n):
        p2, p1 = p1, max(p1, p2 + sticker[i])
    c2 = p1

    return max(c1, c2)