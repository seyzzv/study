def solution(my_string, is_prefix):
    answer = 0
    m = my_string[:len(is_prefix)]
    if m == is_prefix:
        answer = 1
    else: answer = 0
    return answer