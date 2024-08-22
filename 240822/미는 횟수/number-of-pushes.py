a = input()
b = input()

for count in range(len(a)):
    if a[len(a)-count:] + a[:len(a)-count] == b:
        print(count)
        break
else:
    print(-1)