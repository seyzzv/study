def solution(gems):
    total = len(set(gems))
    min_len = len(gems) + 1
    answer = [0, 0]
    counts = {}
    
    left = 0
    for right, gem in enumerate(gems):
        counts[gem] = counts.get(gem, 0) + 1
        
        while len(counts) == total:
            if (right - left + 1) < min_len:
                min_len = right - left + 1
                answer = [left + 1, right + 1]
            
            counts[gems[left]] -= 1
            if counts[gems[left]] == 0:
                del counts[gems[left]]
            left += 1

    return answer