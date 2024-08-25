N, M = map(int, input().split())

distance_a, distance_b = [], []

for i in range(N):
    v, t = map(int, input().split())
    for _ in range(t):
        if distance_a:
            distance_a.append(v + distance_a[-1])
        else:
            distance_a.append(v)

for i in range(M):
    v, t = map(int, input().split())
    for _ in range(t):
        if distance_b:
            distance_b.append(v + distance_b[-1])
        else:
            distance_b.append(v)

result = 0
current_combination = ""
for i in range(len(distance_a)):
    if distance_a[i] > distance_b[i]:
        if current_combination != "A":
            result += 1
        current_combination = "A"
    elif distance_a[i] == distance_b[i]:
        if current_combination != "AB":
            result += 1
        current_combination = "AB"
    else:
        if current_combination != "B":
            result += 1
        current_combination = "B"
print(result)