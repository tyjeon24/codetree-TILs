N, S = map(int, input().split())
numbers = list(map(int, input().split()))
total = sum(numbers)

result = total

for i in range(N-1):
    for j in range(i+1, N):
        sub_total = total - numbers[i] - numbers[j]
        result = min(result, abs(sub_total - S))
print(result)