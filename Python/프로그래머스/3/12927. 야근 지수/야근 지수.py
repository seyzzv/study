import heapq
def solution(n, works):
    if sum(works) <= n:
        return 0
    
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    for _ in range(n):
        largest = heapq.heappop(heap)
        largest += 1
        heapq.heappush(heap, largest)
    
    return sum(x*x for x in heap)