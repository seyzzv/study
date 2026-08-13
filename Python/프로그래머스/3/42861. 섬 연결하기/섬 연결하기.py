def solution(n, costs):
    costs.sort(key=lambda x: x[2])
    
    parent = [i for i in range(n)]
    
    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x
            return True
        return False

    total_cost = 0
    bridge_count = 0

    for start, end, cost in costs:
        if union(start, end):
            total_cost += cost
            bridge_count += 1
            
            if bridge_count == n - 1:
                break
                
    return total_cost