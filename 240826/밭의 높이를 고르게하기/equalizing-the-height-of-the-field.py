import sys

INT_MAX = sys.maxsize

n, h, t = map(int, input().split())
arr = list(map(int, input().split()))

result = INT_MAX
for i in range(n-t):
    sub_arr = arr[i:i+t]

    price = 0
    for j in sub_arr:
        price += abs(j-h)
    result = min(result, price)
print(result)