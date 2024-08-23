n = int(input())
arr = list(map(int, input().split()))

for i, num in enumerate(arr):
    if i%2==0:
        if i==0:
        print(sorted(arr[:i+1])[(i+1)//2], end=" ")