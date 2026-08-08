def solution(n, results):
    matrix = [[False] * (n + 1) for _ in range(n + 1)]
    
    for win, lose in results:
        matrix[win][lose] = True
        
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if matrix[i][k] and matrix[k][j]:
                    matrix[i][j] = True
                    
    answer = 0
    
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if matrix[i][j] or matrix[j][i]:
                count += 1
                
        if count == n - 1:
            answer += 1
            
    return answer