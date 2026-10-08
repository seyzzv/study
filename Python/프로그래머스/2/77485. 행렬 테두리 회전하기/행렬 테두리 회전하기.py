def solution(rows, columns, queries):
    matrix = [[r * columns + c + 1 for c in range(columns)] for r in range(rows)]
    answer = []
    
    for x1, y1, x2, y2 in queries:
        r1, c1, r2, c2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
        
        temp = matrix[r1][c1]
        min_val = temp
        
        for r in range(r1, r2):
            matrix[r][c1] = matrix[r + 1][c1]
            min_val = min(min_val, matrix[r][c1])
            
        for c in range(c1, c2):
            matrix[r2][c] = matrix[r2][c + 1]
            min_val = min(min_val, matrix[r2][c])
            
        for r in range(r2, r1, -1):
            matrix[r][c2] = matrix[r - 1][c2]
            min_val = min(min_val, matrix[r][c2])
            
        for c in range(c2, c1 + 1, -1):
            matrix[r1][c] = matrix[r1][c - 1]
            min_val = min(min_val, matrix[r1][c])
            
        matrix[r1][c1 + 1] = temp
        answer.append(min_val)
        
    return answer