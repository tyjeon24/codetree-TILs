from collections import deque

class Queue:
    def __init__(self):
        self.dq = deque()

    def push(self, item):
        self.dq.append(item)

    def size(self):
        return len(self.dq)

    def empty(self):
        return len(self.dq) == 0

    def pop(self):
        if self.empty():
            raise Exception("Queue is empty")

        return self.dq.popleft()

    def front(self):
        if self.empty():
            raise Exception("Queue is empty")
        
        return self.dq[0]

queue = Queue()
for _ in range(int(input())):
    command = input()

    if command.startswith("push"):
        queue.push(int(command.split()[1]))

    elif command.startswith("pop"):
        print(queue.pop())

    elif command.startswith("size"):
        print(queue.size())
        
    elif command.startswith("empty"):
        print(1 if queue.empty() else 0)
        
    elif command.startswith("front"):
        print(queue.front())