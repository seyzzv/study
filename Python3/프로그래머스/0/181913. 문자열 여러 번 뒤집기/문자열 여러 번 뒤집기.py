def solution(my_string, queries):
    my_string = list(my_string)
    for i, j in queries:
        my_string[i:j+1] = my_string[i:j+1][::-1]
    answer = ''.join(my_string)
    return answer