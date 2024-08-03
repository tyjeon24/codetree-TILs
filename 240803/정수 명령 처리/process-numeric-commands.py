class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def empty(self):
        return 0 if self.items else 1
    
    def size(self):
        return len(self.items)

    def top(self):
        if self.empty():
            raise Exception("Empty")
        return self.items[-1]

    def pop(self):
        if self.empty():
            raise Exception("Empty")
        last = self.items[-1]
        self.items = self.items[:-1]
        return last

stack = Stack()
for i in range(int(input())):
    command = input()

    if command.startswith("push"):
        item = int(command.split()[-1])
        stack.push(item)
    elif command.startswith("pop"):
        print(stack.pop())
    elif command.startswith("size"):
        print(stack.size())
    elif command.startswith("empty"):
        print(stack.empty())
    elif command.startswith("top"):
        print(stack.top())