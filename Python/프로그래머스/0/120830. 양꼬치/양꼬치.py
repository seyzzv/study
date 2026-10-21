def solution(n, k):
    lamb_total = n * 12000
    service_drink = n // 10
    
    drink_total = (k - service_drink) * 2000
    return lamb_total + drink_total