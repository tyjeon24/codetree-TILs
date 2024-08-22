n, m = map(int, input().split())
l, r = 1, 1
while n*l != m*r:
    if n*l > m*r:
        r += 1
    else:
        l+=1
print(n*l)