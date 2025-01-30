class Stack:

    s = []

    def push(self, item):
        self.s.append(item)

    def pop(self):
        return self.s.pop(-1)

    def is_empty(self):
        return not len(self.s)
        