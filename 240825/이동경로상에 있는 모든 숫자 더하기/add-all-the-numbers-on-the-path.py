N, T = map(int, input().split())
DELTAS = [[-1,0], [0,1], [1,0], [0,-1], ]
i = 0

commands = input()

matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
pos = [N//2, N//2]
result = matrix[pos[0]][pos[1]]
for command in commands:
    if command=="F":
        if 0<=pos[0] + DELTAS[i][0]<N and 0<=pos[1] + DELTAS[i][1]<N:
            pos = [pos[0] + DELTAS[i][0], pos[1] + DELTAS[i][1]]
            result += matrix[pos[0]][pos[1]]
    elif command == "R":
        i+=1
    else:
        i-=1
    if i<0:
        i=3
    elif i>4:
        i=0
print(result)