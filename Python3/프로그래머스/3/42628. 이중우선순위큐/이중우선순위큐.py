import heapq

def solution(operations):
    min_h, max_h = [], []
    valid = {}

    for i, op in enumerate(operations):
        cmd, num = op.split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(min_h, (num, i))
            heapq.heappush(max_h, (-num, i))
            valid[i] = True
        elif num == 1:
            while max_h:
                _, idx = heapq.heappop(max_h)
                if idx in valid:
                    del valid[idx]
                    break
        else:
            while min_h:
                _, idx = heapq.heappop(min_h)
                if idx in valid:
                    del valid[idx]
                    break

    while min_h and min_h[0][1] not in valid: heapq.heappop(min_h)
    while max_h and max_h[0][1] not in valid: heapq.heappop(max_h)

    return [-max_h[0][0], min_h[0][0]] if valid else [0, 0]