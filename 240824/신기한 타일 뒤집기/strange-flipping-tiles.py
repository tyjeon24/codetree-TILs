from collections import deque

queue = deque()
idx = 0
for _ in range(int(input())):
    number, direction = input().split()
    for i in range(int(number)):
        if direction == "L":
            if idx >= len(queue):
                idx = len(queue) - 1
            if len(queue) == 0 or idx == -1:
                queue.appendleft("L")
            else:
                queue[idx] = "L"
                idx -= 1
        else:
            if idx < 0:
                idx = 0
            if len(queue) == 0 or idx == len(queue):
                queue.append("R")
                idx = len(queue)
            else:
                queue[idx] = "R"
                idx+=1
        print(queue)
            
queue = list(queue)
print(queue.count("L"), queue.count("R"))