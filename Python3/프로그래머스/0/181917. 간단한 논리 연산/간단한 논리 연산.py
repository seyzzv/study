def solution(x1, x2, x3, x4):
    left = x1 or x2
    right = x3 or x4
    result = left and right
    return result
