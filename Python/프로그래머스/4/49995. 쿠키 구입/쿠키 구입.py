def solution(cookie):
    answer = 0
    n = len(cookie)
    
    for m in range(n - 1):
        l = m
        r = m + 1
        
        sum_left = cookie[l]
        sum_right = cookie[r]
        
        while True:
            if sum_left == sum_right:
                answer = max(answer, sum_left)
                
            if sum_left <= sum_right and l > 0:
                l -= 1
                sum_left += cookie[l]
            elif sum_left >= sum_right and r < n - 1:
                r += 1
                sum_right += cookie[r]
            else:
                break
                
    return answer