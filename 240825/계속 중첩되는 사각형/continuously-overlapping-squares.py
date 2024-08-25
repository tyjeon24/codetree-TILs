n = int(input())
matrix = [[0 for _ in range(201)] for _ in range(201)]

for i in range(n):
    x1, y1, x2, y2 =  map(int, input().split())
    for x in range(x1+100+1, x2+100+1):
        for y in range(y1+100+1, y2+100+1):
            matrix[x][y] = i%2
result = 0
for r in range(len(matrix)):
    result+=sum(matrix[r])
print(result)