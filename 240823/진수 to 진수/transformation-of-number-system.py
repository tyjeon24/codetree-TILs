a, b = map(int, input().split())
n = input()

decimal = 0

for i, num in enumerate(reversed(n)):
    decimal += int(num) * a ** i


converted = []
while True:
    converted.insert(0, str(decimal%b))
    decimal//=b
    if decimal<b:
        converted.insert(0, str(decimal))
        break
print(int("".join(converted)))