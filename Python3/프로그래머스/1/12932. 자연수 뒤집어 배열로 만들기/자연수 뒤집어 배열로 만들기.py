def solution(n):
    answer = []
    n_s = str(n)
    for i in range(len(n_s) - 1, -1, -1):
        answer.append(int(n_s[i]))
    return answer