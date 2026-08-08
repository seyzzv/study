def solution(n, t, m, p):
    digits = "0123456789ABCDEF"
    
    sequence = ""
    num = 0
    while len(sequence) < t * m:
        temp = ""
        x = num
        
        if x == 0:
            temp = "0"
        else:
            while x > 0:
                temp = digits[x % n] + temp
                x //= n
        
        sequence += temp
        num += 1
    
    answer = ""
    for i in range(t):
        answer += sequence[p - 1 + i * m]
    
    return answer