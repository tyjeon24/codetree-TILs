a, b = map(int, input().split())


for number in range(2, 10, 2):
    for i in range(b, a-1, -1):
        print(f"{i} * {number} = {i*number}", end = "")
        if i != a:
            print(" / ", end="")
    print()