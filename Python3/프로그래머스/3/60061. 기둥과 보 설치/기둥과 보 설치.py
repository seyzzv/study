def check(ans):
    for x, y, a in ans:
        if a == 0:
            if y == 0 or (x, y - 1, 0) in ans or (x, y, 1) in ans or (x - 1, y, 1) in ans:
                continue
            return False
        else:
            if (x, y - 1, 0) in ans or (x + 1, y - 1, 0) in ans or ((x - 1, y, 1) in ans and (x + 1, y, 1) in ans):
                continue
            return False
    return True

def solution(n, build_frame):
    ans = set()
    
    for x, y, a, b in build_frame:
        item = (x, y, a)
        if b == 1:
            ans.add(item)
            if not check(ans):
                ans.remove(item)
        else:
            ans.remove(item)
            if not check(ans):
                ans.add(item)
                
    return [list(x) for x in sorted(ans)]