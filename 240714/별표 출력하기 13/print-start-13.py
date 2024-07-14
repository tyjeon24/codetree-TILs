n = int(input())

# 규칙
# n-0 -> 1 -> n-1 -> 2 -> n-3 -> 3 -> ... 순으로 반복
# 이떄 n번 행에 도착 시 규칙 반대로 적용 : n-i -> i -> ...

# 대칭
# 5 기준 3 2 4 1 5
# 홀수 번 : N//2+1 ~ N 까지 출력 : n//2+1 ~ 
# 짝수 번 : N//2 ~ 1 까지 출력

next_odd_stars = n
next_even_stars = 1

for i in range(n):
    if i%2==0:
        print("* "*next_odd_stars)
        next_odd_stars -= 1
    else:
        print("* "*next_even_stars)
        next_even_stars += 1

next_odd_stars += 1
next_even_stars -= 1

for i in range(n):
    if i%2==0:
        print("* "*next_odd_stars)
        next_odd_stars += 1
    else:
        print("* "*next_even_stars)
        next_even_stars -= 1