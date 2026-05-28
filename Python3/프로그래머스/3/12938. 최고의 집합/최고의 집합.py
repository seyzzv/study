def solution(n, s):
    if s < n:
        return [-1]
    base = s // n
    remainder = s % n
    answer = [base] * n
    for i in range(n - remainder, n):
        answer[i] += 1
    return answer