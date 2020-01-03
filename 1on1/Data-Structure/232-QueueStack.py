class MyQueue(object):

    def __init__(self):
        self.list1 = []

    def push(self, x):
        if not self.list1:
            self.list1.append(x)
        else:
            self.list1 = self.reverse(self.list1)
            self.list1.append(x)
            self.list1 = self.reverse(self.list1)

    def pop(self):
        if not self.list1:
            return None
        return self.list1.pop()

    def peek(self):
        if not self.list1:
            return None
        return self.list1[-1]

    def empty(self):
        return len(self.list1) == 0

    def reverse(self, list):
        if not list:
            return []
        else:
            newlist = []
            for i in range(len(list)):
                newlist.append(list.pop())
            return newlist


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
