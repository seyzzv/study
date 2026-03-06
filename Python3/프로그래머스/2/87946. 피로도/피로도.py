def solution(k, d):
    v = [0]*len(d)
    ans = 0
    
    def dfs(p, c):
        nonlocal ans
        ans = max(ans, c)
        
        for i in range(len(d)):
            if not v[i] and p >= d[i][0]:
                v[i] = 1
                dfs(p - d[i][1], c + 1)
                v[i] = 0
    
    dfs(k, 0)
    return ans