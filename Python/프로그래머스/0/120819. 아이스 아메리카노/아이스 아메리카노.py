def solution(money):
    coffee_price = 5500
    cups = money // coffee_price
    change = money % coffee_price
    
    return [cups, change]