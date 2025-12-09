def solution(arr):
    result = arr[:]
    i = 1
    while i < len(arr):
        i *= 2
    j = i - len(arr)
    for _ in range(j):
        result.append(0)
    return result