def solution(ineq, eq, n, m):
    if ((ineq == '>' and eq == '=' and n >= m) or
    (ineq == '<' and eq == '=' and n <= m) or
    (ineq == '>' and eq == '!' and n > m) or
    (ineq == '<' and eq == '!' and n < m)):
        answer = 1
    else:
        answer = 0
    return answer