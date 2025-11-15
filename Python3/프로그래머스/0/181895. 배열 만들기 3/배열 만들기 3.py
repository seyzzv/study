def solution(arr, intervals):
    a1, b1 = intervals[0]
    a2, b2 = intervals[1]
    first_part = arr[a1:b1+1]
    second_part = arr[a2:b2+1]
    return first_part + second_part
