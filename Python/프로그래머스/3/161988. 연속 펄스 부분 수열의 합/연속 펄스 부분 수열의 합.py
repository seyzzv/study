def solution(sequence):
    s1_max = s1_cur = 0
    s2_max = s2_cur = 0
    
    s1_max = s1_cur = sequence[0] * 1
    s2_max = s2_cur = sequence[0] * -1
    
    for i in range(1, len(sequence)):
        p1 = 1 if i % 2 == 0 else -1
        p2 = -p1
        
        val1 = sequence[i] * p1
        val2 = sequence[i] * p2
        s1_cur = max(val1, s1_cur + val1)
        s1_max = max(s1_max, s1_cur)
        s2_cur = max(val2, s2_cur + val2)
        s2_max = max(s2_max, s2_cur)
        
    return max(s1_max, s2_max)