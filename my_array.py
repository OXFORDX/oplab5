class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def isEmpty(self):
        return False if self.stack else True

    def print(self):
        print(self.stack)

    def size(self):
        return len(self.stack)

    def copy(self, array):
        self.stack = array
