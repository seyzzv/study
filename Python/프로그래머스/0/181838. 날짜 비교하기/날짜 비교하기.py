def solution(date1, date2):
    answer = 0
    if tuple(date1) < tuple(date2):
        answer = 1
    return answer