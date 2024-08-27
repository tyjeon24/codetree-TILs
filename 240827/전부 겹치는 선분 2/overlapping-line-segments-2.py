def get_union(l, r):
    if l[1] < r[0]:
        return None
    return (max(l[0], r[0]), min(l[1], r[1]))

n = int(input())
lines = []
for _ in range(n):
    low, high = map(int, input().split())
    lines.append((low, high))
lines.sort()

union = lines[1]
for i in range(2, n-2):
    union = get_union(union, lines[i])
    if union is None:
        print("No")
        break
else:
    if get_union(lines[0], union) or get_union(union, lines[-1]):
        print("Yes")
    else:
        print("No")