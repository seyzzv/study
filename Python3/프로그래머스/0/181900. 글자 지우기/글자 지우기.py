def solution(my_string, indices):
    answer = ''
    indices.sort()
    for i, char in enumerate(my_string):
        if i not in indices:
            answer += char
    return answer