from itertools import combinations
from collections import Counter
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    half = n // 2
    idx_set = set(range(n))
    max_w = -1
    ans = []

    for a_idx in combinations(range(n), half):
        b_idx = tuple(idx_set - set(a_idx))
        
        a_dp = Counter([0])
        for i in a_idx:
            nxt = Counter()
            for s, c in a_dp.items():
                for v in dice[i]:
                    nxt[s + v] += c
            a_dp = nxt
            
        b_dp = Counter([0])
        for i in b_idx:
            nxt = Counter()
            for s, c in b_dp.items():
                for v in dice[i]:
                    nxt[s + v] += c
            b_dp = nxt

        b_sc, b_cnt = zip(*sorted(b_dp.items()))
        b_cum = []
        curr = 0
        for c in b_cnt:
            curr += c
            b_cum.append(curr)

        w_cnt = 0
        for a_sc, a_c in a_dp.items():
            pos = bisect_left(b_sc, a_sc)
            if pos > 0:
                w_cnt += b_cum[pos - 1] * a_c

        if w_cnt > max_w:
            max_w = w_cnt
            ans = a_idx

    return sorted([i + 1 for i in ans])