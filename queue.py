class Queue:
    def __init__(self):
        self.queue = []

    def put(self, item):
        self.queue.insert(0,item)

    def peekLast(self):
        return self.queue[0]

    def peekFirst(self):
        return self.queue[-1]

    def get(self):
        return self.queue.pop()

    def isEmpty(self):
        return self.queue == []

    def clear(self):
        self.queue.clear()
