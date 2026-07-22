def solution(m, n, puddles):
    MOD = 1000000007
    p = set(map(tuple, puddles))
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[1][1] = 1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if (i, j) == (1, 1) or (i, j) in p:
                continue
            dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD

    return dp[m][n]