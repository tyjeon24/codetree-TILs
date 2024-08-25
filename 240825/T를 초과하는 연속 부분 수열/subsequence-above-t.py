n, t = map(int, input().split())
arr = list(map(int, input().split()))

max_length = 0
current_arr = []
for num in arr:
    if num > t:
        current_arr.append(num)
    else:
        max_length = max(max_length, len(current_arr))
        current_arr = []
print(max(max_length, len(current_arr)))