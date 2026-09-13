from collections import deque

def solution(nodes, edges):
    adj = {node: [] for node in nodes}
    deg = {node: 0 for node in nodes}
    
    for u, v in edges:
        adj[u].append(v)
        adj[v].append(u)
        deg[u] += 1
        deg[v] += 1

    visited = set()
    hol_jjak_cnt = 0
    yeok_hol_jjak_cnt = 0

    for node in nodes:
        if node in visited:
            continue
        
        queue = deque([node])
        visited.add(node)
        
        type_a_cnt = 0
        type_b_cnt = 0
        
        while queue:
            curr = queue.popleft()
            
            if (curr % 2) == (deg[curr] % 2):
                type_a_cnt += 1
            else:
                type_b_cnt += 1
                
            for nxt in adj[curr]:
                if nxt not in visited:
                    visited.add(nxt)
                    queue.append(nxt)
        
        if type_a_cnt == 1:
            hol_jjak_cnt += 1
            
        if type_b_cnt == 1:
            yeok_hol_jjak_cnt += 1

    return [hol_jjak_cnt, yeok_hol_jjak_cnt]