def solution(myString):
    answer = []
    for part in myString.split('x'):
        answer.append(len(part))
    return answer