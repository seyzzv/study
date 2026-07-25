from collections import deque, defaultdict

def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    dist[1] = 0

    q = deque([1])
    while q:
        curr = q.popleft()
        for nxt in graph[curr]:
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1
                q.append(nxt)

    max_dist = max(dist)
    return dist.count(max_dist)