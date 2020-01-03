class MinStack(object):
    def __init__(self):
        self.list = []

    def push(self, x):
        self.list.append(x)

    def pop(self):
        if not self.list:
            return None
        else:
            self.list.pop()

    def top(self):
        if not self.list:
            return None
        else:
            return self.list[-1]

    def getMin(self):
        if not self.list:
            return None
        else:
            return min(self.list)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
