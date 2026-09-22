def solution(arr):
    answer = [0, 0]
    
    def compress(x, y, size):
        first = arr[x][y]
        is_same = True
        
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first:
                    is_same = False
                    break
            if not is_same:
                break
                
        if is_same:
            answer[first] += 1
            return
        
        half = size // 2
        compress(x, y, half)
        compress(x + half, y, half)
        compress(x, y + half, half)
        compress(x + half, y + half, half)

    compress(0, 0, len(arr))
    return answer