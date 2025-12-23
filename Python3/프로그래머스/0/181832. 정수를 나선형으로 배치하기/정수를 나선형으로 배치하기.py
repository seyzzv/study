def solution(n):
    answer = [[0]*n for _ in range(n)]
    x = y = d = 0
    for i in range(1, n*n + 1):
        answer[x][y] = i
        nx, ny = x + [0,1,0,-1][d], y + [1,0,-1,0][d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n or answer[nx][ny]:
            d = (d + 1) % 4
            nx, ny = x + [0,1,0,-1][d], y + [1,0,-1,0][d]
        x, y = nx, ny
    return answer