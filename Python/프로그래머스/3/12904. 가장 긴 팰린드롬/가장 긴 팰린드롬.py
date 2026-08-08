def solution(s):
    if len(s) < 2:
        return len(s)
    
    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    max_len = 1
    
    for i in range(len(s) - 1):
        len1 = expand(i, i)
        len2 = expand(i, i + 1)
        max_len = max(max_len, len1, len2)
        
    return max_len