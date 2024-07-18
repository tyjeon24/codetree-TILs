string = input()
new_string = []

for i, char in enumerate(string):
    if i%2 == 1:
        new_string.append(char)

while new_string:
    print(new_string.pop(), end="")