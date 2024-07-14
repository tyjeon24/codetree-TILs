N = int(input())
for i in range(N):
    number = int(input())
    if number % 2 == 1 and number % 3 == 0:
        print(number)