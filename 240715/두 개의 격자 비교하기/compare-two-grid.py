n, m = map(int, input().split())

matrix_1 = []
matrix_2 = []
for i in range(n):
    matrix_1.append(list(map(int, input().split())))
for i in range(n):
    matrix_2.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if matrix_1[i][j] == matrix_2[i][j]:
            print(0, end=" ")
        else:
            print(1, end=" ")
    print()