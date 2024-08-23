from collections import deque

queue = deque([0])
idx = 0
for _ in range(int(input())):
    number, direction = input().split()
    for i in range(int(number)):
        if direction == "L":
            if idx == 0:
                queue.appendleft("L")
            else:
                queue[idx] = "L"
                idx -= 1
        else:
            if idx == len(queue)-1:
                queue.append("R")
            else:
                queue[idx] = "R"
                idx+=1
            
queue = list(queue)
print(queue.count("L"), queue.count("R"))