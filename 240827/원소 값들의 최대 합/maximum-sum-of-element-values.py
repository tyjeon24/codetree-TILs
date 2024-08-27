n, m = map(int, input().split())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse=True)

print(sum(arr[:m]))