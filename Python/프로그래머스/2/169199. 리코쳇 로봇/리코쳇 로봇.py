from collections import deque

def solution(board):
    n = len(board)
    m = len(board[0])
    
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                start = (i, j)
            elif board[i][j] == 'G':
                goal = (i, j)
                
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    def get_next_position(x, y, d):
        nx, ny = x, y
        while True:
            nnx = nx + dx[d]
            nny = ny + dy[d]
            if 0 <= nnx < n and 0 <= nny < m and board[nnx][nny] != 'D':
                nx, ny = nnx, nny
            else:
                break
        return nx, ny

    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * m for _ in range(n)]
    visited[start[0]][start[1]] = True
    
    while queue:
        x, y, count = queue.popleft()
        
        if (x, y) == goal:
            return count
            
        for d in range(4):
            nx, ny = get_next_position(x, y, d)
            
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, count + 1))
                
    return -1