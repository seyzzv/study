def solution(s):
    trans_cnt = 0
    del_cnt = 0
    while s != '1':
        zero_cnt = 0
        for ch in s:
            if ch == '0':
                zero_cnt += 1
        del_cnt += zero_cnt
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        trans_cnt += 1
    return [trans_cnt, del_cnt]