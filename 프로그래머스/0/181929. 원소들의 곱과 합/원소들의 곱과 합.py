def solution(num_list):
    a, b = 1, 0
    for i in num_list:
        a *= i
        b += i
    if a > b**2:
        answer = 0
    else:
        answer = 1
    
    return answer