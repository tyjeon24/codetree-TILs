from collections import deque


stack = deque()

for string in input():
    if string == "(":
        stack.append("(")

    elif string == ")":
        if len(stack):
            stack.pop()
        else:
            print("No")
            break
else:
    if len(stack):
        print("No")
    else:
        print("Yes")