arr = {}
idx = 0
delta = {"L":-1, "R":1}

for _ in range(int(input())):
    number, direction = input().split()
    for _ in range(int(number)):
        arr[idx] = direction
        idx += delta[direction]
    idx += -delta[direction]

arr = list(arr.values())
print(arr.count("L"), arr.count("R"))