n, m = map(int, input().split())
arr = list(map(int, input().split()))


result = 0
for index in range(n):
    temp = 0
    next_index = index
    for _ in range(m):
        temp += arr[next_index]
        next_index = arr[next_index]-1
    result = max(result, temp)
print(result)