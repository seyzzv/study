def solution(n_str):
    answer = '' 
    isTF = False
    for i in n_str:
        if i != '0': isTF = True
        if isTF: answer += i
    if answer == '': answer = '0'
    return answer