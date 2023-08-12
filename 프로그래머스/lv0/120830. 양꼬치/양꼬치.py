def solution(n, k):
    yang_price = 12000
    beverage = 2000
    
    total = (yang_price * n) + (beverage * k) - (n // 10 * beverage)
    
    
    return total