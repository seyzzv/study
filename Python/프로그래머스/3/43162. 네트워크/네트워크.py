def solution(n, computers):
    visited = [0] * n
    answer = 0
    def dfs(x):
        visited[x] = 1
        for i in range(n):
            if computers[x][i] and not visited[i]:
                dfs(i)
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    return answer