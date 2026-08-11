def solution(target):
    score_map = {}
    
    for i in range(1, 21):
        score_map[i * 2] = 0
        score_map[i * 3] = 0
        
    for i in range(1, 21):
        score_map[i] = 1
    score_map[50] = 1
    
    scores = list(score_map.items())

    dp = [[float('inf'), 0] for _ in range(target + 1)]
    dp[0] = [0, 0]

    for i in range(target):
        if dp[i][0] == float('inf'):
            continue
            
        cnt, sb = dp[i]
        
        for score, is_sb in scores:
            next_score = i + score
            if next_score > target:
                continue
                
            n_cnt = cnt + 1
            n_sb = sb + is_sb
            
            if n_cnt < dp[next_score][0]:
                dp[next_score] = [n_cnt, n_sb]
            elif n_cnt == dp[next_score][0] and n_sb > dp[next_score][1]:
                dp[next_score][1] = n_sb

    return dp[target]