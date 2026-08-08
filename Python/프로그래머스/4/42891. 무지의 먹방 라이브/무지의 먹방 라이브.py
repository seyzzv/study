import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    q = [(t, i + 1) for i, t in enumerate(food_times)]
    heapq.heapify(q)
    
    total = 0
    prev = 0
    n = len(q)
    
    while total + ((q[0][0] - prev) * n) <= k:
        now, _ = heapq.heappop(q)
        total += (now - prev) * n
        n -= 1
        prev = now
        
    q.sort(key=lambda x: x[1])
    
    return q[(k - total) % n][1]