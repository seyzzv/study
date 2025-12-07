def solution(arr):
    answer = []
    for x in arr:
        if answer and answer[-1] == x:
            answer.pop()
        else:
            answer.append(x)
    return answer if answer else [-1]