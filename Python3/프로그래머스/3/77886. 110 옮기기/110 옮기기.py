def solution(s):
    ans = []
    
    for str_val in s:
        st = []
        cnt = 0
        
        for c in str_val:
            st.append(c)
            if len(st) >= 3 and st[-3] == '1' and st[-2] == '1' and st[-1] == '0':
                del st[-3:]
                cnt += 1
                
        idx = len(st) - 1
        while idx >= 0 and st[idx] != '0':
            idx -= 1
            
        ins = ['1', '1', '0'] * cnt
        st[idx + 1:idx + 1] = ins
        ans.append("".join(st))
        
    return ans