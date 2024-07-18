e_removed = False

for i in input():
    if not e_removed and i == "e":
        e_removed = True
        continue
    print(i, end="")