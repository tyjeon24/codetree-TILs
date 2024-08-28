n = int(input())
arr = sorted((map(int, input().split())))
# 가능한 방법 1 : 정렬된 순서대로 2개씩 묶기
method_1 = [arr[i+n]-arr[i] for i in range(n)]

# 가능한 방법 2 : (i, i+n) 쌍으로 만들기
method_2 = [arr[i+1]-arr[i] for i in range(0, 2*n-1, 2)]

result = max(min(method_1), min(method_2))
print(result)