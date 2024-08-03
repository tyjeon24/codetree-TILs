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



n, k = map(int, input().split())

queue = Queue()
for i in range(1, n+1):
    queue.push(i)

while queue.size():
    for _ in range(k-1):
        queue.push(queue.pop())
    print(queue.pop(), end=" ")