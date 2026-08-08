def is_match(user, banned):
    if len(user) != len(banned):
        return False
    
    for u, b in zip(user, banned):
        if b != '*' and u != b:
            return False
    return True

def solution(user_id, banned_id):
    visited = [False] * len(user_id)
    result_sets = set()
    
    def dfs(banned_idx, current_selection):
        if banned_idx == len(banned_id):
            result_sets.add(tuple(sorted(current_selection)))
            return
        
        current_banned = banned_id[banned_idx]
        
        for i, user in enumerate(user_id):
            if not visited[i] and is_match(user, current_banned):
                visited[i] = True
                dfs(banned_idx + 1, current_selection + [user])
                visited[i] = False

    dfs(0, [])
    
    return len(result_sets)