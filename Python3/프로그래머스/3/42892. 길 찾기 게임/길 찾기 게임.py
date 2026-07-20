import sys
sys.setrecursionlimit(10 ** 6)

def solution(nodeinfo):
    nodes = sorted([(x, y, i + 1) for i, (x, y) in enumerate(nodeinfo)], key=lambda n: (-n[1], n[0]))
    pre_arr, post_arr = [], []
    
    def traverse(curr):
        if not curr:
            return
        
        x, _, idx = curr[0]
        pre_arr.append(idx)
        
        traverse([n for n in curr[1:] if n[0] < x])
        traverse([n for n in curr[1:] if n[0] > x])
        
        post_arr.append(idx)
        
    traverse(nodes)
    return [pre_arr, post_arr]