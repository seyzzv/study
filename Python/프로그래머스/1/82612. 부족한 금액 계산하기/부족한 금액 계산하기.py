def solution(price, money, count):
    total_price = price * count * (count + 1) // 2
    return total_price - money if total_price > money else 0