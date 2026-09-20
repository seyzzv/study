def solution(arr):
    min_val = min(arr)
    result = [x for x in arr if x != min_val]
    return result if result else [-1]