def solution(n, m, x, y, queries):
    r1, r2 = x, x
    c1, c2 = y, y
    
    for command, dx in reversed(queries):
        if command == 0:
            if c1 != 0:
                c1 += dx
            c2 = min(m - 1, c2 + dx)
        elif command == 1:
            if c2 != m - 1:
                c2 -= dx
            c1 = max(0, c1 - dx)
        elif command == 2:
            if r1 != 0:
                r1 += dx
            r2 = min(n - 1, r2 + dx)
        elif command == 3:
            if r2 != n - 1:
                r2 -= dx
            r1 = max(0, r1 - dx)
            
        if r1 >= n or r2 < 0 or c1 >= m or c2 < 0:
            return 0
            
    return (r2 - r1 + 1) * (c2 - c1 + 1)