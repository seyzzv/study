def solution(beginning, target):
    n = len(beginning)
    m = len(beginning[0])
    answer = float('inf')

    for row_mask in range(1 << n):
        row_flip_count = 0
        
        board = [row[:] for row in beginning]
        
        for i in range(n):
            if (row_mask >> i) & 1:
                row_flip_count += 1
                for j in range(m):
                    board[i][j] ^= 1
        
        col_flip_count = 0
        for j in range(m):
            if board[0][j] != target[0][j]:
                col_flip_count += 1
                for i in range(n):
                    board[i][j] ^= 1
        
        possible = True
        for i in range(n):
            for j in range(m):
                if board[i][j] != target[i][j]:
                    possible = False
                    break
            if not possible:
                break
        
        if possible:
            answer = min(answer, row_flip_count + col_flip_count)

    return answer if answer != float('inf') else -1