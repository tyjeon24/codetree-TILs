# 학생 n명
# 예산 b
n, b = map(int, input().split())

# 가격 p, 배송비 s
prices = []
for _ in range(n):
    price, shipping = map(int, input().split())
    prices.append((price + shipping, price, shipping))

result = 0
for coupon_target in range(n):
    new_prices = [p for p in prices]
    new_prices[coupon_target] = (
        new_prices[coupon_target][0]-new_prices[coupon_target][1]//2,
        new_prices[coupon_target][1]//2,
        new_prices[coupon_target][2]
        )
    new_prices.sort()
    budget = b
    presents = 0
    for i in range(n):
        if budget < new_prices[i][0]:
            break
        budget -= new_prices[i][0]
        presents += 1
        result = max(result, presents)
print(result)