def solution(a):
    n = len(a)
    if n <= 2:
        return n
    
    l = [0] * n
    l[0] = a[0]
    for i in range(1, n):
        l[i] = min(l[i-1], a[i])
        
    r = [0] * n
    r[n-1] = a[n-1]
    for i in range(n-2, -1, -1):
        r[i] = min(r[i+1], a[i])
        
    ans = 0
    for i in range(n):
        if a[i] <= l[i] or a[i] <= r[i]:
            ans += 1
            
    return ans