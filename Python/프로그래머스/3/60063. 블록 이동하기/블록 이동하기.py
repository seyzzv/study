from collections import deque

def get_next_pos(pos, new_board):
    next_pos = []
    pos = list(pos)
    r1, c1 = pos[0]
    r2, c2 = pos[1]
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    for i in range(4):
        nr1, nc1 = r1 + dr[i], c1 + dc[i]
        nr2, nc2 = r2 + dr[i], c2 + dc[i]
        if new_board[nr1][nc1] == 0 and new_board[nr2][nc2] == 0:
            next_pos.append({(nr1, nc1), (nr2, nc2)})
            
    if r1 == r2:
        for d in [-1, 1]: 
            if new_board[r1 + d][c1] == 0 and new_board[r2 + d][c2] == 0:
                next_pos.append({(r1, c1), (r1 + d, c1)})
                next_pos.append({(r2, c2), (r2 + d, c2)})
                
    elif c1 == c2:
        for d in [-1, 1]:
            if new_board[r1][c1 + d] == 0 and new_board[r2][c2 + d] == 0:
                next_pos.append({(r1, c1), (r1, c1 + d)})
                next_pos.append({(r2, c2), (r2, c2 + d)})
                
    return next_pos

def solution(board):
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
            
    start = {(1, 1), (1, 2)}
    queue = deque([(start, 0)])
    visited = [start]
    
    while queue:
        pos, time = queue.popleft()
        
        if (n, n) in pos:
            return time
            
        for next_p in get_next_pos(pos, new_board):
            if next_p not in visited:
                visited.append(next_p)
                queue.append((next_p, time + 1))
                
    return 0