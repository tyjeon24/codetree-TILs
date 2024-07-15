n = int(input())
number = 0

for i in range(n):
    for j in range(n):
        number += 1
        if i%2==1:
            number += 1
        print(number, end=" ")

    print()