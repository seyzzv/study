def solution(s):
    ans = []
    parsed = s[2:-2].split("},{")
    
    lst = []
    for x in parsed:
        lst.append(list(map(int, x.split(','))))
        
    lst.sort(key=len)
    
    seen = set()
    for row in lst:
        for val in row:
            if val not in seen:
                ans.append(val)
                seen.add(val)
                break
                
    return ans