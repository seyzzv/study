
def solution(a, edges):
    n = len(a)
    graph = [[] for _ in range(n)]

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    parent = [-1] * n
    order = [0]

    for node in order:
        for nxt in graph[node]:
            if nxt != parent[node]:
                parent[nxt] = node
                order.append(nxt)

    if sum(a) != 0:
        return -1

    answer = 0

    for node in reversed(order[1:]):
        answer += abs(a[node])
        a[parent[node]] += a[node]

    return answer