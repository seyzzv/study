def solution(x):
    s = str(x)
    n = 0
    for i in s:
        n += int(i)
    if x % n == 0:
        return True
    else:
        return False