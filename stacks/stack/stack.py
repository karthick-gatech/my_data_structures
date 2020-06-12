from collections import deque
myStack = deque()
myStack.append('a')
myStack.append('b')

print myStack
print myStack.pop()
print myStack

class Stack:
    def __init__(self):
        self.items = deque()

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print s.size()
print s.pop()
print s.isEmpty()