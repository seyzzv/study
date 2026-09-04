import math

def solution(n, k):
    answer = []
    numbers = list(range(1, n + 1))
    
    k -= 1
    
    for i in range(n, 0, -1):
        fact = math.factorial(i - 1)
        
        idx = k // fact
        answer.append(numbers.pop(idx))
        
        k %= fact
        
    return answer