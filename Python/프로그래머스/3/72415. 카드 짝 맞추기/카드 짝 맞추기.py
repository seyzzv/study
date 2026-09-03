from collections import deque
from itertools import permutations
import copy

DR = [-1, 1, 0, 0]
DC = [0, 0, -1, 1]

def move_ctrl(board, r, c, dr, dc):
    nr, nc = r + dr, c + dc
    while 0 <= nr < 4 and 0 <= nc < 4:
        if board[nr][nc] != 0:
            return nr, nc
        nr += dr
        nc += dc
    return nr - dr, nc - dc

def bfs(board, start, target):
    if start == target:
        return 0
    
    queue = deque([(start[0], start[1], 0)])
    visited = [[False] * 4 for _ in range(4)]
    visited[start[0]][start[1]] = True
    
    while queue:
        r, c, dist = queue.popleft()
        
        if (r, c) == target:
            return dist
        
        for i in range(4):
            nr, nc = r + DR[i], c + DC[i]
            if 0 <= nr < 4 and 0 <= nc < 4 and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, dist + 1))
            
            cr, cc = move_ctrl(board, r, c, DR[i], DC[i])
            if not visited[cr][cc]:
                visited[cr][cc] = True
                queue.append((cr, cc, dist + 1))

def solution(board, r, c):
    card_pos = {}
    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num > 0:
                if num not in card_pos:
                    card_pos[num] = []
                card_pos[num].append((i, j))
                
    card_types = list(card_pos.keys())
    min_total_moves = float('inf')
    
    for order in permutations(card_types):
        temp_board = copy.deepcopy(board)
        cur_pos = (r, c)
        total_moves = 0
        
        for card_num in order:
            p1, p2 = card_pos[card_num]
            
            cost1 = bfs(temp_board, cur_pos, p1) + bfs(temp_board, p1, p2) + 2
            cost2 = bfs(temp_board, cur_pos, p2) + bfs(temp_board, p2, p1) + 2
            
            if cost1 < cost2:
                total_moves += cost1
                cur_pos = p2
            else:
                total_moves += cost2
                cur_pos = p1
                
            temp_board[p1[0]][p1[1]] = 0
            temp_board[p2[0]][p2[1]] = 0
            
        min_total_moves = min(min_total_moves, total_moves)
        
    return min_total_moves