def solution(alp, cop, problems):
    ma, mc = 0, 0
    for ar, cr, _, _, _ in problems:
        if ar > ma: ma = ar
        if cr > mc: mc = cr
        
    alp = alp if alp < ma else ma
    cop = cop if cop < mc else mc
    
    if alp == ma and cop == mc:
        return 0
        
    INF = 10**9
    dp = [[INF] * (mc + 1) for _ in range(ma + 1)]
    dp[alp][cop] = 0
    
    for i in range(alp, ma + 1):
        for j in range(cop, mc + 1):
            c_cost = dp[i][j]
            if c_cost == INF:
                continue
                
            if i < ma and c_cost + 1 < dp[i + 1][j]:
                dp[i + 1][j] = c_cost + 1
            if j < mc and c_cost + 1 < dp[i][j + 1]:
                dp[i][j + 1] = c_cost + 1
                
            for ar, cr, aw, cw, cost in problems:
                if i >= ar and j >= cr:
                    na = i + aw if i + aw < ma else ma
                    nc = j + cw if j + cw < mc else mc
                    
                    if c_cost + cost < dp[na][nc]:
                        dp[na][nc] = c_cost + cost
                        
    return dp[ma][mc]