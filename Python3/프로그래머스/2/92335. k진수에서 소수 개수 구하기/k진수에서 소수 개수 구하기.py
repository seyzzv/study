def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    base_k_str = ""
    while n > 0:
        base_k_str = str(n % k) + base_k_str
        n //= k
        
    candidates = base_k_str.split("0")

    answer = 0
    for cand in candidates:
        if cand:
            if is_prime(int(cand)):
                answer += 1

    return answer