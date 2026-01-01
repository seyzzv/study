def solution(n):
    c = n & -n
    r = n + c
    return (((r ^ n) >> 2) // c) | r