def solution(my_string, indices):
    my_string = list(my_string)
    for i in sorted(indices, reverse = True):
        del my_string[i]
    return ''.join(my_string)