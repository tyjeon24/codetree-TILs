# 학생 n명
# 예산 b
n, b = map(int, input().split())

# 가격 p, 배송비 s
prices = []
for _ in range(n):
    price, shipping = map(int, input().split())
    prices.append((price + shipping, price, shipping))

prices.sort()

result = 0
for coupon_target in range(n):
    new_prices = prices
    new_prices[coupon_target] = (new_prices[coupon_target][0]-new_prices[coupon_target][1]//2, 0, 0)
    new_prices.sort()
    budget = b
    presents = 0
    for i in range(n):
        if budget < new_prices[i][0]:
            result = max(result, presents)
            break
        else:
            budget -= new_prices[i][0]
            presents += 1
    result = max(result, presents)
print(result)