import sys

result = sys.maxsize

n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_value, max_value = min(arr), max(arr)
for target in range(min_value, max_value+1):
    temp = 0
    for num in arr:
        temp += min(abs(min_value-num), abs(max_value-num))
    result = min(result, temp)
print(result)