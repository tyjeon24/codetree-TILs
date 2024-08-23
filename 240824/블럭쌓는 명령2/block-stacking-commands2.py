N, K = map(int, input().split())
arr = [0 for _ in range(N)]

for _ in range(K):
    a, b = map(int, input().split())
    for i in range(a-1, b):
        arr[i] += 1
print(max(arr))