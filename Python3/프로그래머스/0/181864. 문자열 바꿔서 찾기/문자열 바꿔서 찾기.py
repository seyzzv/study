def solution(myString, pat):
    answer = 0
    ab = myString.translate(str.maketrans({'A':'B','B':'A'}))
    if pat in ab:
        answer = 1
    return answer