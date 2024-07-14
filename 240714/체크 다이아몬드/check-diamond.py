n = int(input())

# 총 길이 = 2n-1
# 현재 행 값을 i로 가정(1부터 시작)
# 1번 : 필요한 별 i개, 공간 (n-i)개 주고 별 공백 반복
# 2번 : i개, 공간 (n-i)개 주고 별 공백 반복

for i in range(1, n+1):
    print(" " * (n-i), end="")
    for j in range(i):
        print("* ", end = "")
    print()

for i in range(n-1, 0, -1):
    print(" " * (n-i), end="")
    for j in range(i):
        print("* ", end = "")
    print()