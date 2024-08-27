n = int(input())
lines = []
for _ in range(n):
    low, high = map(int, input().split())
    lines.append((low, high))

lines.sort()
result = "No"

# 선을 비교
low = lines[0][1]
for i in range(n-2):
    left, right = lines[i], lines[i+1]
    
    if low < right[0]: # 안 겹치면 break
        break
    # 두 선 중 더 작은 high 값이 모든 선의 교차점
    low = min(left[1], right[1])

else:
    result = "Yes"
low = lines[1][1]
for i in range(1, n-1):
    left, right = lines[i], lines[i+1]
    
    if low < right[0]: # 안 겹치면 break
        break
    # 두 선 중 더 작은 high 값이 모든 선의 교차점
    low = min(left[1], right[1])

else:
    result = "Yes"
print(result)