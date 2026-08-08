def find(node, parent):
    if node not in parent:
        parent[node] = node + 1
        return node
    
    path = []
    while node in parent:
        path.append(node)
        node = parent[node]
        
    for p in path:
        parent[p] = node + 1
        
    parent[node] = node + 1
    return node

def solution(k, room_number):
    parent = {}
    return [find(num, parent) for num in room_number]