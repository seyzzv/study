from collections import Counter

def solution(weights):
    answer = 0
    counter = Counter(weights)
    
    for w in counter:
        if counter[w] > 1:
            answer += counter[w] * (counter[w] - 1) // 2
        
        if w * 1.5 in counter:
            answer += counter[w] * counter[w * 1.5]
        if w * 2.0 in counter:
            answer += counter[w] * counter[w * 2.0]
        if (w * 4 / 3) in counter:
            answer += counter[w] * counter[w * 4 / 3]
            
    return answer