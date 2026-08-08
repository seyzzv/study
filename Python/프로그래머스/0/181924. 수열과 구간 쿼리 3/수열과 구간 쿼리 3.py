def solution(arr, queries):
    for i in queries:
        a = i[0]
        b = i[1]
        c = arr[a]
        arr[a] = arr[b]
        arr[b] = c
    return arr