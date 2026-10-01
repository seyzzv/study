def solution(n, m, section):
    answer = 0
    current_painted = 0
    
    for sec in section:
        if sec > current_painted:
            answer += 1
            current_painted = sec + m - 1
            
    return answer