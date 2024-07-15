n = int(input())

for _ in range(n):
    result = 0
    a, b = map(int, input().split())
    for j in range(a, b+1):
        if j%2==0:
            result += j
    print(result)