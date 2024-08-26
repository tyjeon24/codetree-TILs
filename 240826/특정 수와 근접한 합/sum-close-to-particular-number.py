N, S = map(int, input().split())
numbers = list(map(int, input().split()))
total = sum(numbers)
result = S

for i in range(N):
    for j in range(i+1, N):
        sub_total = total - numbers[i]- numbers[j]
        
        if abs(sub_total-S) < result:
            result = abs(sub_total-S)
    
print(result)