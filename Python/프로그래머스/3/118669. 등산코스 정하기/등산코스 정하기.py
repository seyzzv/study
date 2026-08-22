import heapq

def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for u, v, w in paths:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    gate_set = set(gates)
    summit_set = set(summits)
    
    INF = float('inf')
    intensity = [INF] * (n + 1)
    
    pq = []
    
    for gate in gates:
        intensity[gate] = 0
        heapq.heappush(pq, (0, gate))
    
    while pq:
        cur_intensity, u = heapq.heappop(pq)
        
        if cur_intensity > intensity[u]:
            continue
            
        if u in summit_set:
            continue
            
        for v, w in graph[u]:
            if v in gate_set:
                continue
                
            next_intensity = max(cur_intensity, w)
            if next_intensity < intensity[v]:
                intensity[v] = next_intensity
                heapq.heappush(pq, (next_intensity, v))
    
    result = [0, INF]
    for summit in sorted(summits):
        if intensity[summit] < result[1]:
            result = [summit, intensity[summit]]
            
    return result