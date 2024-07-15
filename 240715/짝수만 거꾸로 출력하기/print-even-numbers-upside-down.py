input()
numbers = []
for number in map(int, input().split()):
    if number % 2 == 0:
        numbers.append(number)
while numbers:
    print(numbers.pop(), end=" ")