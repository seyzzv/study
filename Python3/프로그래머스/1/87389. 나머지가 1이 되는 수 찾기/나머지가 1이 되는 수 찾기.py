def solution(n):
    answer = 0
    is_bool = True
    i = 0
    while is_bool:
        i += 1
        if n % i == 1:
            answer = i
            is_bool = False
    return answer