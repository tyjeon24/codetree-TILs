a, b = map(int, input().split())

remainder_counter = [0 for _ in range(10)]

while a>1:
    remainder_counter[a%b] += 1
    a//=b

result = 0
for remainder in remainder_counter:
    result += remainder**2
print(result)