a = input()
order = input()
start_index = 0

for command in order:
    if command == "L":
        start_index += 1
    else:
        start_index -= 1

if start_index < 0:
    start_index += len(a)
for i in range(start_index, len(a)):
    print(a[i], end="")
if start_index != 0:
    for i in range(0, start_index):
        print(a[i], end="")