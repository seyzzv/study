def solution(info, edges):
    n = len(info)
    graph = [[] for _ in range(n)]
    for p, c in edges:
        graph[p].append(c)
        
    max_sheep = 1
    visited = [False] * (1 << n)
    visited[1] = True
    
    queue = [(1, 1, 0, 1)]
    
    for state, sheep, wolf, usable in queue:
        if sheep > max_sheep:
            max_sheep = sheep
            
        for i in range(n):
            if state & (1 << i):
                for child in graph[i]:
                    if not (state & (1 << child)):
                        next_state = state | (1 << child)
                        if not visited[next_state]:
                            n_sheep = sheep + (1 if info[child] == 0 else 0)
                            n_wolf = wolf + (1 if info[child] == 1 else 0)
                            
                            if n_sheep > n_wolf:
                                visited[next_state] = True
                                queue.append((next_state, n_sheep, n_wolf, i))
                                
    return max_sheep