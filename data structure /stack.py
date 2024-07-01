class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):

        self.stack.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def content(self):
        for item in self.stack:
            if item is not None:
                print(item)


stack = Stack()

print(stack.isEmpty())
for i in range(1, 100, 5):
    stack.push(i)
print(stack.isEmpty())
print(stack.size())
stack.content()
print(stack.pop())
print(stack.peek())


