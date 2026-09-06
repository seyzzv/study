def solution(maze):
    n = len(maze)
    m = len(maze[0])
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    red_start, blue_start = None, None
    red_end, blue_end = None, None
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 1:
                red_start = (i, j)
            elif maze[i][j] == 2:
                blue_start = (i, j)
            elif maze[i][j] == 3:
                red_end = (i, j)
            elif maze[i][j] == 4:
                blue_end = (i, j)

    r_visited = [[False] * m for _ in range(n)]
    b_visited = [[False] * m for _ in range(n)]
    
    r_visited[red_start[0]][red_start[1]] = True
    b_visited[blue_start[0]][blue_start[1]] = True
    
    INF = float('inf')
    min_turns = INF

    def dfs(rx, ry, bx, by, turn):
        nonlocal min_turns
        
        if turn >= min_turns:
            return
            
        r_end = (rx, ry) == red_end
        b_end = (bx, by) == blue_end
        if r_end and b_end:
            min_turns = min(min_turns, turn)
            return

        r_nexts = []
        if r_end:
            r_nexts.append((rx, ry))
        else:
            for i in range(4):
                nr, mr = rx + dx[i], ry + dy[i]
                if 0 <= nr < n and 0 <= mr < m and maze[nr][mr] != 5 and not r_visited[nr][mr]:
                    r_nexts.append((nr, mr))

        b_nexts = []
        if b_end:
            b_nexts.append((bx, by))
        else:
            for i in range(4):
                nb, mb = bx + dx[i], by + dy[i]
                if 0 <= nb < n and 0 <= mb < m and maze[nb][mb] != 5 and not b_visited[nb][mb]:
                    b_nexts.append((nb, mb))

        for nrx, nry in r_nexts:
            for nbx, nby in b_nexts:
                if (nrx, nry) == (nbx, nby):
                    continue
                
                if (nrx, nry) == (bx, by) and (nbx, nby) == (rx, ry):
                    continue
                
                r_visited[nrx][nry] = True
                b_visited[nbx][nby] = True
                
                dfs(nrx, nry, nbx, nby, turn + 1)
                
                if not r_end:
                    r_visited[nrx][nry] = False
                if not b_end:
                    b_visited[nbx][nby] = False

    dfs(red_start[0], red_start[1], blue_start[0], blue_start[1], 0)

    return min_turns if min_turns != INF else 0