def solution(arr, divisor):
    result = []
    for num in arr:
        if num % divisor == 0:
            result.append(num)
    if len(result) == 0:
        return [-1]
    result.sort()
    return result
