from itertools import combinations
from bisect import bisect_left

def solution(dice):
    n = len(dice)
    half = n // 2
    idx_set = set(range(n))
    max_w = -1
    ans = []

    for a_idx in combinations(range(n), half):
        b_idx = tuple(idx_set - set(a_idx))
        
        a_dp = [0] * 501
        a_dp[0] = 1
        for i in a_idx:
            nxt = [0] * 501
            for s in range(501):
                if a_dp[s]:
                    for v in dice[i]:
                        nxt[s + v] += a_dp[s]
            a_dp = nxt
            
        b_dp = [0] * 501
        b_dp[0] = 1
        for i in b_idx:
            nxt = [0] * 501
            for s in range(501):
                if b_dp[s]:
                    for v in dice[i]:
                        nxt[s + v] += b_dp[s]
            b_dp = nxt

        b_sc, b_cnt = [], []
        for s in range(501):
            if b_dp[s]:
                b_sc.append(s)
                b_cnt.append(b_dp[s])

        b_cum = []
        curr = 0
        for c in b_cnt:
            curr += c
            b_cum.append(curr)

        w_cnt = 0
        for s in range(501):
            if a_dp[s]:
                pos = bisect_left(b_sc, s)
                if pos > 0:
                    w_cnt += b_cum[pos - 1] * a_dp[s]

        if w_cnt > max_w:
            max_w = w_cnt
            ans = a_idx

    return sorted([i + 1 for i in ans])