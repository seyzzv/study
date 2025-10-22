def solution(a, d, included):
    result = 0
    for i in range(len(included)):
        answer = a + i*d
        if included[i]:
            result += answer
    return result