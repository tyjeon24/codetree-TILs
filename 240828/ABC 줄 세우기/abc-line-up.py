n = int(input())
arr = list(input().split())

result = 0
for i in range(n):
    for j in range(i+1, n):
        if ord(arr[i]) > ord(arr[j]):
            result += 1
            arr[i], arr[j] = arr[j], arr[i]

print(result)