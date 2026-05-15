from collections import Counter

def solution(a):
    if len(a) < 2:
        return 0
    
    counts = Counter(a)
    answer = 0
    
    for k, v in counts.items():
        if v * 2 <= answer:
            continue
        
        count = 0
        i = 0
        while i < len(a) - 1:
            if (a[i] != k and a[i+1] != k) or (a[i] == a[i+1]):
                i += 1
                continue
            
            count += 2
            i += 2
            
        answer = max(answer, count)
        
    return answer