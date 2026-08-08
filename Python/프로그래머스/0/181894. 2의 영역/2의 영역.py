def solution(arr):
    answer = []
    positions = []
    for i in range(len(arr)):
        if arr[i] == 2:
            positions.append(i)
    if not positions:
        return [-1]
    answer = arr[positions[0]:positions[-1]+1]
    return answer
