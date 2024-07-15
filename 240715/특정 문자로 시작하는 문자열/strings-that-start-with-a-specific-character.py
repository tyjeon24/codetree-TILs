n = int(input())
strings = [input() for _ in range(n)]
alphabet = input()
count = 0
result = 0
for string in strings:
    if string[0] == alphabet:
        count += 1
        result += len(string)
print(f"{count} {result/count:.2f}")