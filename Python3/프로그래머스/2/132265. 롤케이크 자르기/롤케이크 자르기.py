from collections import Counter

def solution(topping):
    answer = 0
    left_set = set()
    right_map = Counter(topping)
    
    for t in topping:
        left_set.add(t)
        right_map[t] -= 1
        
        if right_map[t] == 0:
            del right_map[t]
            
        if len(left_set) == len(right_map):
            answer += 1
            
    return answer