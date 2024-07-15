n = int(input())

number = 65

for i in range(n):
    for j in range(n):
        if j<i:
            print(" ", end=" ")
        else:
            print(chr(number), end=" ")
            number += 1
    print()