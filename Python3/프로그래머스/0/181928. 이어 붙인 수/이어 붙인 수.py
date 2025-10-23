def solution(num_list):
    a, b = '', ''
    for i in num_list:
        if i % 2 == 0:
            a += str(i)
        elif i % 2 == 1:
            b += str(i)
    return int(a) + int(b)