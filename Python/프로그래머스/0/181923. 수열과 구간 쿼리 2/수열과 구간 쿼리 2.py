def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        sub_arr = arr[s:e+1]
        candidates = [x for x in sub_arr if x > k]
        
        if not candidates:
            answer.append(-1)
        else:
            answer.append(min(candidates))
    return answer
