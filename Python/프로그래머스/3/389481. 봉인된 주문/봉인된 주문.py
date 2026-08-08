import bisect

def solution(n, bans):
    def str_to_idx(s):
        idx = 0
        for i in range(1, len(s)):
            idx += 26 ** i
        val = 0
        for c in s:
            val = val * 26 + (ord(c) - ord('a'))
        return idx + val + 1

    def idx_to_str(idx):
        L = 1
        while idx > 26 ** L:
            idx -= 26 ** L
            L += 1
        idx -= 1
        res = []
        for _ in range(L):
            res.append(chr(ord('a') + (idx % 26)))
            idx //= 26
        return "".join(reversed(res))

    bi = sorted([str_to_idx(b) for b in bans])
    
    low = 1
    high = n + len(bi)
    ans = high
    
    while low <= high:
        mid = (low + high) // 2
        cnt = bisect.bisect_right(bi, mid)
        
        if mid - cnt >= n:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
            
    answer = idx_to_str(ans)
    return answer