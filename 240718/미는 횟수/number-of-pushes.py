a = input()
b = input()

for count in range(len(a)):
    if a[count:] + a[:count] == b:
        print(count)
        break
else:
    print(-1)