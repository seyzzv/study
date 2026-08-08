def solution(arr, k):
    result = []
    for num in arr:
        if num not in result:
            result.append(num)
            if len(result) == k:
                break
    while len(result) < k:
        result.append(-1)
    return result