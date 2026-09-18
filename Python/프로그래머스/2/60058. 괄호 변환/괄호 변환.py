def solution(p):
    if not p:
        return ""
    
    balance = 0
    split_index = 0
    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1
        if balance == 0:
            split_index = i + 1
            break
            
    u = p[:split_index]
    v = p[split_index:]
    
    is_correct = True
    temp_balance = 0
    for char in u:
        if char == '(':
            temp_balance += 1
        else:
            temp_balance -= 1
        if temp_balance < 0:
            is_correct = False
            break
            
    if is_correct:
        return u + solution(v)
    else:
        res = "(" + solution(v) + ")"
        
        middle = u[1:-1]
        flipped = []
        for char in middle:
            if char == '(':
                flipped.append(')')
            else:
                flipped.append('(')
                
        res += "".join(flipped)
        
        return res