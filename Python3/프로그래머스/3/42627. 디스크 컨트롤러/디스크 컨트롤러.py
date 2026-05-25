import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    
    total, now, i, count = 0, 0, 0, 0
    n = len(jobs)
    q = []
    
    while count < n:
        while i < n and jobs[i][0] <= now:
            start, term = jobs[i]
            heapq.heappush(q, (term, start))
            i += 1
            
        if q:
            term, start = heapq.heappop(q)
            now += term
            total += (now - start)
            count += 1
        else:
            now = jobs[i][0]
            
    return total // n