def solution(my_string):
    result = [0] * 52  
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            result[ord(ch) - ord('A')] += 1
        elif 'a' <= ch <= 'z':
            result[ord(ch) - ord('a') + 26] += 1
    return result