n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for row in range(n):
    for col in range(n):
        first_row_or_first_col = row == 0 or col == 0
        if first_row_or_first_col:
            matrix[row][col] = 1
        else:
            matrix[row][col] = matrix[row-1][col-1] + matrix[row-1][col] + matrix[row][col-1] 


for row in range(n):
    for col in range(n):
        print(matrix[row][col], end=" ")
    print()