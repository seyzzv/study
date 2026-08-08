def solution(n):
    answer = 0
    k = 1
    while k * (k - 1) // 2 < n:
        if (n - k * (k - 1) // 2) % k == 0:
            answer += 1
        k += 1
    return answer