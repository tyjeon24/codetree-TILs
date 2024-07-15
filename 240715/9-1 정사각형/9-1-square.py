n = int(input())
number = 9

for i in range(n):
    for j in range(n):
        print(number, end="")
        number -= 1
        if number == 0:
            number = 9
    print()