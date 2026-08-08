def solution(enroll, referral, seller, amount):
    parent_map = {}
    money_map = {}
    
    for en, ref in zip(enroll, referral):
        parent_map[en] = ref
        money_map[en] = 0
        
    for s, a in zip(seller, amount):
        current_profit = a * 100
        current_user = s
        
        while current_user != "-" and current_profit > 0:
            to_parent = current_profit // 10

            to_mine = current_profit - to_parent

            money_map[current_user] += to_mine
            
            current_user = parent_map[current_user]
            current_profit = to_parent
            
  
    return [money_map[name] for name in enroll]