n = int(input())


segments = []
for _ in range(n):
    x1, x2 = map(int, input().split())
    segments.append((x1, 1))
    segments.append((x2, -1))

max_overlap = 0

current_overlap = 0
for point, value in sorted(segments):
    current_overlap += value 
    max_overlap = max(max_overlap, current_overlap)
print(max_overlap)