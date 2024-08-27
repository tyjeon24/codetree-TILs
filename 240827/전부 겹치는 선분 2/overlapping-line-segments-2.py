lines = []
for _ in range(int(input())):
    low, high = map(int, input().split())
    lines.append((low, high))

lines.sort()
result = "No"
prev_low, prev_high = lines[0]
for line in lines[1:-1]:
    current_low, current_high = line
    if current_low > prev_high:
        break
    prev_low, prev_high = line
else:
    result = "Yes"


prev_low, prev_high = lines[1]
for line in lines[2:]:
    current_low, current_high = line
    if current_low > prev_high:
        break
    prev_low, prev_high = line
else:
    result = "Yes"
print(result)