def solution(num_list):
    result = []
    for i in range(len(num_list)-1, -1, -1):
        result.append(num_list[i])
    return result
# return num_list[::-1]