n = int(input())
cnt = 0
while n < 1000:
    n = n*2+2 if n%2 else n*3+1
    cnt+=1
print(cnt)