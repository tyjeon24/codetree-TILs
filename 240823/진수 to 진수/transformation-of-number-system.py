a, b = map(int, input().split())
n = input()

decimal = 0

for i, num in enumerate(reversed(n)):
    decimal += int(num) * a ** i



while True:
    print(decimal%b, end="")
    decimal//=b
    if decimal<b:
        print(decimal)
        break