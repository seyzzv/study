from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[-1] * 102 for _ in range(102)]
    
    for r in rectangle:
        x1, y1, x2, y2 = [v * 2 for v in r]
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                if x1 < x < x2 and y1 < y < y2:
                    board[x][y] = 0
                elif board[x][y] != 0:
                    board[x][y] = 1

    cx, cy, ix, iy = characterX * 2, characterY * 2, itemX * 2, itemY * 2
    q = deque([(cx, cy)])
    board[cx][cy] = 1

    while q:
        x, y = q.popleft()
        if x == ix and y == iy:
            return (board[x][y] - 1) // 2

        for dx, dy in ((-1,0), (1,0), (0,-1), (0,1)):
            nx, ny = x + dx, y + dy
            if board[nx][ny] == 1:
                board[nx][ny] = board[x][y] + 1
                q.append((nx, ny))