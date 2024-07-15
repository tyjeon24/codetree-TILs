input()
result = 100
numbers = list(map(int, input().split()))
for index in range(len(numbers)):
    if index >= 1:
        result = numbers[index] - numbers[index-1] if numbers[index] - numbers[index-1] < result else result
print(result)