import sys
sys.setrecursionlimit(10**6)


def solution(n, lighthouse):
    adj = [[] for _ in range(n + 1)]
    for u, v in lighthouse:
        adj[u].append(v)
        adj[v].append(u)

    visited = [False] * (n + 1)
    ans = 0

    def dfs(u):
        nonlocal ans
        visited[u] = True

        need_light = False

        for neighbor in adj[u]:
            if not visited[neighbor]:
                child_is_on = dfs(neighbor)

                if not child_is_on:
                    need_light = True

        if need_light:
            ans += 1
            return True
        return False

    dfs(1)

    return ans