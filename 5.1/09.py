class Queue:

    q = []

    def push(self, item):
        self.q.append(item)

    def pop(self):
        return self.q.pop(0)

    def is_empty(self):
        return not len(self.q)
        