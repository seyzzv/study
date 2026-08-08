def solution(s):
    n = len(s)
    pair = {')': '(', ']': '[', '}': '{'}
    answer = 0

    for x in range(n):
        rotated = s[x:] + s[:x]
        stack = []
        valid = True
        for ch in rotated:
            if ch in '([{':
                stack.append(ch)
            else:
                if not stack or stack[-1] != pair[ch]:
                    valid = False
                    break
                stack.pop()
        if valid and not stack:
            answer += 1
    return answer