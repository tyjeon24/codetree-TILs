n = int(input())
for i in range(1, n):
    n = n//i
    if n < 1:
        break
print(i)