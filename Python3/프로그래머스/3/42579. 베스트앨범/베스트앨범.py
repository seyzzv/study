from collections import defaultdict

def solution(genres, plays):
    total = defaultdict(int)
    best = defaultdict(list)
    
    for i, (genre, play) in enumerate(zip(genres, plays)):
        total[genre] += play
        best[genre].append((play, i))
        
        best[genre].sort(key=lambda x: (-x[0], x[1]))
        if len(best[genre]) > 2:
            best[genre].pop()
    
    answer = []
    for genre in sorted(total, key=lambda x: total[x], reverse=True):
        for play, idx in best[genre]:
            answer.append(idx)
            
    return answer