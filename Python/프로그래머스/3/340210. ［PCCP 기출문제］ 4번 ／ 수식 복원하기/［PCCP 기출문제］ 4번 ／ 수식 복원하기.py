def to_decimal(num_str, base):
    return int(num_str, base)

def from_decimal(num, base):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % base))
        num //= base
    return "".join(reversed(digits))

def solution(expressions):
    max_digit = 0
    for expr in expressions:
        for char in expr:
            if char.isdigit():
                max_digit = max(max_digit, int(char))
    
    min_base = max(2, max_digit + 1)
    possible_bases = list(range(min_base, 10))

    valid_expressions = []
    target_expressions = []

    for expr in expressions:
        A, op, B, eq, C = expr.split()
        if C == "X":
            target_expressions.append((A, op, B, expr))
        else:
            valid_expressions.append((A, op, B, C))

    filtered_bases = []
    for b in possible_bases:
        is_valid = True
        for A, op, B, C in valid_expressions:
            a_dec = to_decimal(A, b)
            b_dec = to_decimal(B, b)
            c_dec = to_decimal(C, b)
            
            if op == '+' and a_dec + b_dec != c_dec:
                is_valid = False
                break
            elif op == '-' and a_dec - b_dec != c_dec:
                is_valid = False
                break
        
        if is_valid:
            filtered_bases.append(b)

    result = []
    for A, op, B, orig_expr in target_expressions:
        results_set = set()
        for b in filtered_bases:
            a_dec = to_decimal(A, b)
            b_dec = to_decimal(B, b)
            res_dec = (a_dec + b_dec) if op == '+' else (a_dec - b_dec)
            res_base = from_decimal(res_dec, b)
            results_set.add(res_base)
        
        if len(results_set) == 1:
            ans = results_set.pop()
        else:
            ans = "?"
            
        result.append(f"{A} {op} {B} = {ans}")

    return result