def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        answer += (a + i*d) * included[i]
    return answer