def solution(arr):
    answer = []
    for i in range(max(len(arr), len(arr[0]))):
        row = []
        for j in range(max(len(arr), len(arr[0]))):
            if i < len(arr) and j < len(arr[0]):
                row.append(arr[i][j])
            else:
                row.append(0)
        answer.append(row)
    return answer