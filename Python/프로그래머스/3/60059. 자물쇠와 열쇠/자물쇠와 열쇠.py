def rotate_90(matrix):
    n = len(matrix)
    m = len(matrix[0])
    result = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = matrix[i][j]
    return result

def check(new_lock, n):
    for i in range(n, n * 2):
        for j in range(n, n * 2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    m = len(key)
    n = len(lock)
    
    new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            new_lock[i + n][j + n] = lock[i][j]
            
    for _ in range(4):
        key = rotate_90(key)
        for x in range(n * 2):
            for y in range(n * 2):
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] += key[i][j]
                if check(new_lock, n):
                    return True
                for i in range(m):
                    for j in range(m):
                        new_lock[x + i][y + j] -= key[i][j]
                        
    return False