from collections import Counter
def solution(want, number, discount):
    want_map = Counter(dict(zip(want, number)))
    window = Counter(discount[:10])
    answer = 0
    if window == want_map:
        answer += 1
    for i in range(10, len(discount)):
        window[discount[i]] += 1
        window[discount[i - 10]] -= 1
        if window[discount[i - 10]] == 0:
            del window[discount[i - 10]]
        if window == want_map:
            answer += 1
    return answer