from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque([(0, 0, 1)])
    
    maps[0][0] = 0
    
    while queue:
        y, x, dist = queue.popleft()

        if y == n - 1 and x == m - 1:
            return dist
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                queue.append((ny, nx, dist + 1))
                
    return -1