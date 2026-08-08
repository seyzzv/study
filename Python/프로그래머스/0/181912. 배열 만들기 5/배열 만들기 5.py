def solution(intStrs, k, s, l):
    answer = []
    for num_str in intStrs:
        sub_str = num_str[s:s + l]
        sub_int = int(sub_str)
        if sub_int > k:
            answer.append(sub_int)
    return answer
