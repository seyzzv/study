def solution(a, b, g, s, w, t):
    left, right = 0, 10**15

    while left < right:
        mid = (left + right) // 2

        gold = 0
        silver = 0
        total = 0

        for i in range(len(g)):
            cnt = (mid + t[i]) // (2 * t[i])

            capacity = min(g[i] + s[i], cnt * w[i])

            gold += min(g[i], capacity)
            silver += min(s[i], capacity)
            total += capacity

        if gold >= a and silver >= b and total >= a + b:
            right = mid
        else:
            left = mid + 1

    return left