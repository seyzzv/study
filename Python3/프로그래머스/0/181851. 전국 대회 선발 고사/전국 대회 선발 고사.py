def solution(rank, attendance):
    answer = 0
    result = []
    for i in range(len(rank)):
        if attendance[i]:
            result.append((rank[i], i))
    result.sort()
    answer = 10000 * result[0][1] + 100 * result[1][1] + result[2][1]
    return answer