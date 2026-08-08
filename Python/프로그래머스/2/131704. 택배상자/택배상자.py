def solution(order):
    answer = 0
    stack = []
    current = 1
    
    for target in order:
        while current <= len(order) and current <= target:
            stack.append(current)
            current += 1
        
        if stack and stack[-1] == target:
            stack.pop()
            answer += 1
        else:
            break
    
    return answer