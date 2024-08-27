import sys

result = sys.maxsize

n, k = map(int, input().split())
arr = list(map(int, input().split()))

min_value, max_value = min(arr), max(arr)
for target in range(min_value, max_value+1):
    target_min, target_max = target, target+k
    temp = 0
    for num in arr:
        if target_min <= num <= target_max:
            continue
        temp += min(abs(target_min-num), abs(target_max-num))
    result = min(result, temp)
print(result)