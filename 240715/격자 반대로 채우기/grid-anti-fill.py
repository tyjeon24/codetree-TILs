n = int(input())

matrix = [[0 for _ in range(n)] for _ in range(n)]

number = 1
for index, column in enumerate(range(n-1, -1, -1)):
    if index % 2 == 0:
        for row in range(n-1, -1, -1):
            matrix[row][column] = number
            number += 1
    else:
        for row in range(n):
            matrix[row][column] = number
            number += 1
for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=" ")
    print()