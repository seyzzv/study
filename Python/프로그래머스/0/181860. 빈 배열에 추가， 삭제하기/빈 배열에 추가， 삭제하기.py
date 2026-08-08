def solution(arr, flag):
    answer = []
    for i in range(len(arr)):
        if flag[i]:
            for _ in range(arr[i] * 2):
                answer.append(arr[i])
        else:
            answer = answer[:-arr[i]]
    return answer