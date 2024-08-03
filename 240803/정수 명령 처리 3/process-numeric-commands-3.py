from collections import deque

dq = deque()

for i in range(int(input())):
    command = input()

    if command.startswith("push_front"):
        dq.appendleft(int(command.split()[1]))
    elif command.startswith("push_back"):
        dq.append(int(command.split()[1]))
    elif command.startswith("pop_front"):
        print(dq.popleft())
    elif command.startswith("pop_back"):
        print(dq.pop())
    elif command.startswith("size"):
        print(len(dq))
    elif command.startswith("empty"):
        print(0 if len(dq) else 1)
    elif command.startswith("front"):
        print(dq[0])
    elif command.startswith("back"):
        print(dq[-1])