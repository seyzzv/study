def solution(n, roads, sources, dest):
    g = [[] for _ in range(n + 1)]
    for a, b in roads:
        g[a].append(b)
        g[b].append(a)
    
    d = [-1] * (n + 1)
    d[dest] = 0
    
    q = [dest]
    i = 0
    
    while i < len(q):
        curr = q[i]
        i += 1
        for nxt in g[curr]:
            if d[nxt] == -1:
                d[nxt] = d[curr] + 1
                q.append(nxt)
    
    return [d[s] for s in sources]