from collections import defaultdict
from bisect import bisect_left, bisect_right

def solution(words, queries):
    forward = defaultdict(list)
    backward = defaultdict(list)

    for word in words:
        length = len(word)
        forward[length].append(word)
        backward[length].append(word[::-1])

    for length in forward:
        forward[length].sort()
        backward[length].sort()

    answer = []

    for query in queries:
        length = len(query)

        if query[0] == '?':
            query = query[::-1]
            target = backward[length]
        else:
            target = forward[length]

        left = query.replace('?', 'a')
        right = query.replace('?', 'z')

        count = bisect_right(target, right) - bisect_left(target, left)
        answer.append(count)

    return answer