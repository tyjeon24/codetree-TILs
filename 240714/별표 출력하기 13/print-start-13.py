n = int(input())

# 홀수번째 : n n-1 n-2 n-3 n-3 n-2 n-1 n
# if i > n//2 기점으로 방향 바꾸면 됨
# 짝수번째 : 1

toggle = "even"
even = n
odd = 1
for i in range(n):
    if toggle == "even":
        print("* "*even)
        even -= 1
        toggle = "odd"
    else:
        print("* "*odd)
        odd += 1
        toggle = "even"

toggle = "even" if toggle=="odd" else "odd"
odd -= 1
even += 1

for i in range(n):
    if toggle == "even":
        print("* "*even)
        even += 1
        toggle = "odd"
    else:
        print("* "*odd)
        odd += 1
        toggle = "even"