n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    for j in range(n-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for i in range(n):
    print(numbers[i], end=" ")