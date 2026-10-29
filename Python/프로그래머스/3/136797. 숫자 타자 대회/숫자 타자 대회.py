
def solution(numbers):
    pos = [(3, 1), (0, 0), (0, 1), (0, 2),
           (1, 0), (1, 1), (1, 2),
           (2, 0), (2, 1), (2, 2)]

    dist = [[0] * 10 for _ in range(10)]

    for i in range(10):
        for j in range(10):
            if i == j:
                dist[i][j] = 1
            else:
                dx = abs(pos[i][0] - pos[j][0])
                dy = abs(pos[i][1] - pos[j][1])
                diagonal = min(dx, dy)
                straight = abs(dx - dy)
                dist[i][j] = diagonal * 3 + straight * 2

    dp = {(4, 6): 0}

    for ch in numbers:
        n = int(ch)
        ndp = {}

        for (left, right), cost in dp.items():
            if n == left or n == right:
                key = (left, right)
                ndp[key] = min(ndp.get(key, float('inf')), cost + 1)
            else:
                key = (n, right)
                ndp[key] = min(ndp.get(key, float('inf')), cost + dist[left][n])

                key = (left, n)
                ndp[key] = min(ndp.get(key, float('inf')), cost + dist[right][n])

        dp = ndp

    return min(dp.values())
