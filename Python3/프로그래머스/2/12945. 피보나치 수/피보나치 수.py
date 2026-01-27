def solution(n):
    n_1 = 1
    n_2 = 0
    for _ in range(2, n + 1):
        n_2, n_1 = n_1, (n_1 + n_2) % 1234567
    return n_1