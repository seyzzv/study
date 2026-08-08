def solution(n, m, x, y, r, c, k):
    shortest_dist = abs(x - r) + abs(y - c)
    if shortest_dist > k or (k - shortest_dist) % 2 != 0:
        return "impossible"
    
    dx = [1, 0, 0, -1]
    dy = [0, -1, 1, 0]
    direction_char = ['d', 'l', 'r', 'u']
    
    answer = []
    
    while k > 0:
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 1 <= nx <= n and 1 <= ny <= m:
                next_dist = abs(nx - r) + abs(ny - c)
                
                if next_dist <= k - 1:
                    answer.append(direction_char[i])
                    x, y = nx, ny
                    k -= 1
                    break
                    
    return ''.join(answer)