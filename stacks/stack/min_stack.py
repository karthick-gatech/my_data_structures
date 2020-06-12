class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.minimum = x
        else:
            if x < self.minimum:
                self.stack.append(2 * x - self.minimum)
                self.minimum = x
            else:
                self.stack.append(x)

    def pop(self):
        if self.stack:
            top = self.stack.pop()
            if top < self.minimum:
                print "here"
                self.minimum = 2 * self.minimum - top
            #print self.stack

    def top(self):
        if not self.stack:
            return None
        else:
            top = self.stack[-1]
            if top < self.minimum:
                return self.minimum
            else:
                return top

    def getMin(self):
        if self.stack:
            return self.minimum
        else:
            return None

def main():
    obj = MinStack()
    obj.push(100)
    obj.push(20)
    print obj.stack
    obj.push(10)
    print obj.stack
    obj.push(0)
    print obj.stack
    #print obj.getMin()
    obj.pop()
    print obj.getMin()
    obj.pop()
    print obj.getMin()

main()