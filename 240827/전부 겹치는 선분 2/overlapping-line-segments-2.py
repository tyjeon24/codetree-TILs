import sys

INT_MAX = sys.maxsize
n = int(input())

x1_list, x2_list = [], []

for _ in range(n):
    x1, x2 = tuple(map(int, input().split()))
    x1_list.append(x1)
    x2_list.append(x2)

ans = "No"

for skip in range(n):
    max_x1, min_x2 = 0, INT_MAX
    for i in range(n):
        if i==skip:
            continue

        max_x1 = max(max_x1, x1_list[i])
        min_x2 = min(min_x2, x2_list[i])
    
    if min_x2 >= max_x1:
        ans = "Yes"
    else:
        ans = "No"
print(ans)