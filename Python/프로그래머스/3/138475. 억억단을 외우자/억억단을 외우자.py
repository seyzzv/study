def solution(e, starts):
    count = [0] * (e + 1)

    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            count[j] += 1

    answer = [0] * (e + 2)
    best = e

    for i in range(e, 0, -1):
        if count[i] >= count[best]:
            best = i
        answer[i] = best

    return [answer[s] for s in starts]