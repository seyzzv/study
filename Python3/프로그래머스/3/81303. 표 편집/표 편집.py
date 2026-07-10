def solution(n, k, cmd):
    p = [i - 1 for i in range(n)]
    nt = [i + 1 for i in range(n)]
    nt[-1] = -1
    
    st = []
    curr = k
    
    for c in cmd:
        if c[0] == 'U':
            for _ in range(int(c.split()[1])):
                curr = p[curr]
        elif c[0] == 'D':
            for _ in range(int(c.split()[1])):
                curr = nt[curr]
        elif c[0] == 'C':
            st.append((p[curr], curr, nt[curr]))
            if p[curr] != -1:
                nt[p[curr]] = nt[curr]
            if nt[curr] != -1:
                p[nt[curr]] = p[curr]
            curr = nt[curr] if nt[curr] != -1 else p[curr]
        elif c[0] == 'Z':
            prev_i, r, next_i = st.pop()
            if prev_i != -1:
                nt[prev_i] = r
            if next_i != -1:
                p[next_i] = r
                
    res = ['O'] * n
    for _, r, _ in st:
        res[r] = 'X'
        
    return ''.join(res)