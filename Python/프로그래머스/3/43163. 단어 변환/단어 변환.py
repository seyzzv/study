from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [False] * len(words)
    queue = deque([(begin, 0)])
    
    while queue:
        current, depth = queue.popleft()
        
        if current == target:
            return depth
        
        for i in range(len(words)):
            if not visited[i]:
                diff = 0
                for a, b in zip(current, words[i]):
                    if a != b:
                        diff += 1
                
                if diff == 1:
                    visited[i] = True
                    queue.append((words[i], depth + 1))
    
    return 0