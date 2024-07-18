n = int(input())
result = 0
for i in range(n):
    result += int(input())
print(str(result)[1:] + str(result)[0])