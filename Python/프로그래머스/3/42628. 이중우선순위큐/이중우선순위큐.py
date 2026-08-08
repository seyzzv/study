import heapq

def solution(operations):
    h = []
    
    for op in operations:
        cmd, num = op.split()
        num = int(num)
        
        if cmd == 'I':
            heapq.heappush(h, num)
        elif h:
            if num == 1:
                h.remove(max(h))
                heapq.heapify(h)
            else:
                heapq.heappop(h)
                
    return [max(h), h[0]] if h else [0, 0]