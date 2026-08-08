from collections import deque

def solution(x, y, n):
    visited = [False] * (y + 1)
    q = deque([(x, 0)])
    visited[x] = True
    
    while q:
        cur, cnt = q.popleft()
        
        if cur == y:
            return cnt
        
        for nxt in (cur + n, cur * 2, cur * 3):
            if nxt <= y and not visited[nxt]:
                visited[nxt] = True
                q.append((nxt, cnt + 1))
    
    return -1