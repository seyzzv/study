from collections import Counter
def solution(k, tangerine):
    count = sorted(Counter(tangerine).values(), reverse=True)
    total = 0
    answer = 0
    for i in count:
        total += i
        answer += 1
        if total >= k:
            return answer