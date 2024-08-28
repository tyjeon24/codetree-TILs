n = int(input())

x1_list = []
x2_list = []

result = 200

for _ in range(n):
    x1, x2 = map(int, input().split())
    x1_list.append(x1)
    x2_list.append(x2)

for skip in range(n):
    x1_min = 101
    x2_max = 0
    for i in range(n):
        if i == skip:
            continue
        x1_min = min(x1_min, x1_list[i])
        x2_max = max(x2_max, x2_list[i])
    result = min(result, x2_max-x1_min)

print(result)