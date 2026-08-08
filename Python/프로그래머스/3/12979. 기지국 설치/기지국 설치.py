import math

def solution(n, stations, w):
    answer = 0
    curr = 1 
    step = 2 * w + 1
    
    for s in stations:
        if curr < s - w:
            answer += math.ceil((s - w - curr) / step)
        curr = s + w + 1
        
    if curr <= n:
        answer += math.ceil((n - curr + 1) / step)

    return answer