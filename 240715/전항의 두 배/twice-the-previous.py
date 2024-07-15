numbers = list(map(int, input().split()))

while len(numbers) != 10:
    numbers.append(numbers[-1] + numbers[-2]*2)
for number in numbers:
    print(number, end=" ")