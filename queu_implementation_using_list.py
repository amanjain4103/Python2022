# implement queue using list

class Queue:
    def __init__(self):
        self.queue = []

    def push(self, data):
        self.queue.append(data)

    def pop(self):
        self.queue = self.queue[1:len(self.queue)]

    def __str__(self):
        return self.queue.__str__()


q1 = Queue()
q1.push(10)
q1.push(20)
q1.push(30)
print(q1)
q1.pop()
q1.pop()
print(q1)
