n = int(input())

print("* "*n)
for i in range(1, n):
    left_stars = "* "*i
    padding = 2*n - 2 - len(left_stars)
    print(left_stars + " " * padding + "*")