def solution(n, tops):
    MOD = 10007
    
    a = 0
    b = 1
    
    for top in tops:
        if top == 1:
            next_a = (a + b) % MOD
            next_b = (2 * a + 3 * b) % MOD
        else:
            next_a = (a + b) % MOD
            next_b = (a + 2 * b) % MOD
            
        a, b = next_a, next_b
        
    return (a + b) % MOD