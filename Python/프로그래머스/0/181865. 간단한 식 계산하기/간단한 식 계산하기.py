def solution(binomial):
    answer = 0
    num = binomial.split()
    if num[1] == '+':
        answer = int(num[0]) + int(num[2])
    elif num[1] == '-':
        answer = int(num[0]) - int(num[2])
    elif num[1] == '*':
        answer = int(num[0]) * int(num[2])
    return answer