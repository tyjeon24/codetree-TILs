result = 0
for i in range(4):
    result += sum(list(map(int, input().split()))[:i+1])
print(result)