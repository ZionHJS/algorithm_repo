"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution(object):
    def.__init__(self):
        self.new_head

    def copyRandomList(self, head):
        if not head:
            return []

        self.new_head = Node(int(head.val))

        while head.next():
            head = head.next()
            self.new_head = self.new_head.next

            self.new_head = Node(head.val)
            if head.random == None:
                self.new_head.random = None
            else:
                self.new_head.random = head.next.random
