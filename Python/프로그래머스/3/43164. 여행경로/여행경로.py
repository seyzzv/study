from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)
    for start, end in tickets:
        graph[start].append(end)
    
    for start in graph:
        graph[start].sort(reverse=True)
    
    stack = ["ICN"]
    path = []
    
    while stack:
        top = stack[-1]
        
        if graph[top]:
            stack.append(graph[top].pop())
        else:
            path.append(stack.pop())
            
    return path[::-1]