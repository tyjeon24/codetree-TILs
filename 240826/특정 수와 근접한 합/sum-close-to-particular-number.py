import sys

INT_MAX = sys. maxsize

n, s = map(int, input().split())
arr = list(map(int, input().split()))

array_sum = 0
ans = INT_MAX

for elem in arr:
    array_sum += elem

for i in range(n):
    for j in range(i+1, n):
        new_sum = array_sum - arr[i] - arr[j]
        diff = abs(new_sum - s)
        ans = min(ans, diff)
print(ans)