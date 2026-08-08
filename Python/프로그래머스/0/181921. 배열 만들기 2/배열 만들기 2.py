def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        i = str(i)
        for j in i:
            if j != '0' and j != '5':
                break
        else:
            answer.append(int(i))
    if answer == []:
        return [-1]
    return answer
