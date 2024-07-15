input()
counter = 0
for index, number in enumerate(map(int, input().split())):
    if number == 2:
        counter += 1
    if counter == 3:
        break
print(index + 1)