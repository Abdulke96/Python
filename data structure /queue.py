class Queue:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.isEmpty():
            return self.queue.pop(0)
        return None

    def size(self):
        return len(self.queue)

    def content(self):
        print("QUEUE CONTENT")
        for item in self.queue:
            if item is not None:
                print(item)


queue = Queue()
print(queue.isEmpty())
print(queue.size())
for i in range(10):
    queue.enqueue((i+1)*10)
print(queue.isEmpty())
print(queue.size())
queue.content()

for i in range(queue.size()):
    print(f"{queue.dequeue()} dequeued")

print(queue.isEmpty())
print(queue.size())

