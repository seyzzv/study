def solution(board):
    n = len(board)
    
    def can_drop(r, c):
        for i in range(r):
            if board[i][c] != 0:
                return False
        return True

    def can_erase(r, c, h, w):
        empty_count = 0
        block_id = -1
        
        for i in range(r, r + h):
            for j in range(c, c + w):
                val = board[i][j]
                if val == 0:
                    if not can_drop(i, j):
                        return False
                    empty_count += 1
                else:
                    if block_id == -1:
                        block_id = val
                    elif block_id != val:
                        return False
        
        if empty_count == 2:
            for i in range(r, r + h):
                for j in range(c, c + w):
                    board[i][j] = 0
            return True
        return False

    answer = 0
    
    while True:
        erased = False
        for i in range(n):
            for j in range(n):
                if i + 1 < n and j + 2 < n:
                    if can_erase(i, j, 2, 3):
                        answer += 1
                        erased = True
                        break
                if i + 2 < n and j + 1 < n:
                    if can_erase(i, j, 3, 2):
                        answer += 1
                        erased = True
                        break
            if erased:
                break
        
        if not erased:
            break
            
    return answer