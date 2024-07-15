n, m = map(int, input().split())

matrix = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    row, col = map(int, input().split())
    matrix[row-1][col-1] = row*col

for row in range(n):
    for col in range(n):
        print(matrix[row][col], end=" ")
    print()