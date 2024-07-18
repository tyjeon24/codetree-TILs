a = input()
b = input()

number_a = ""
number_b = ""

for i in a:
    if 65 <= ord(i) <= 125:
        continue
    else:
        number_a += i
for i in b:
    if 65 <= ord(i) <= 125:
        continue
    else:
        number_b += i
print(int(number_a)+int(number_b))