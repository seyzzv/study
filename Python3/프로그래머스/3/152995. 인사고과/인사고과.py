def solution(scores):
    wanho = scores[0]
    wanho_sum = sum(wanho)
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    max_b = 0
    rank = 1
    
    for score in scores:
        if score[1] < max_b:
            if score == wanho:
                return -1
        else:
            max_b = max(max_b, score[1])
            if sum(score) > wanho_sum:
                rank += 1
                
    return rank