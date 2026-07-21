def solution(numbers):
    answer = []
    for x in numbers:
        if x % 2 == 0:
            answer.append(x + 1)
        else:
            lowest_zero = ~x & (x + 1)
            answer.append(x + lowest_zero - (lowest_zero // 2))
            
    return answer