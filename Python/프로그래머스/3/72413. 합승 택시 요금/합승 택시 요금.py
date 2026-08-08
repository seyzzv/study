def solution(n, s, a, b, fares):
    INF = float('inf')
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        graph[i][i] = 0
        
    for c, d, f in fares:
        graph[c][d] = f
        graph[d][c] = f
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    
    min_cost = graph[s][a] + graph[s][b]
    
    for i in range(1, n + 1):
        cost = graph[s][i] + graph[i][a] + graph[i][b]
        if cost < min_cost:
            min_cost = cost
            
    return min_cost