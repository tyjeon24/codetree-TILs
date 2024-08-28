n = int(input())
arr = list(map(int, input().split()))

arr = sorted(arr)

result = max(arr[0]*arr[1]*arr[-1], arr[-3]*arr[-2]*arr[-1])
print(result)