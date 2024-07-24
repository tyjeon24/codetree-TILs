n = int(input())
numbers = list(map(int, input().split()))

for i in range(n):
    min_index = i
    for j in range(i, n):
        if numbers[j] < numbers[min_index]:
            min_index = j
    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

for i in range(n):
    print(numbers[i], end=" ")