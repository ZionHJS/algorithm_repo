"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
import queue


class Solution:
    def __init__(self):
        self.res = []

    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return self.res
        elif not root.left and not root.right:
            return [root.val, "#"]

        self.bfs(root)
        return self.res

    def bfs(self, root):
        q = queue.Queue()
        q.put(root)

        while q.qsize():
            for i in range(q.qsize()):
                cur_node = q.get()
                if cur_node != None:
                    if cur_node.left:
                        q.put(cur_node.left)
                    if cur_node.right:
                        q.put(cur_node.right)
                    self.res.append(cur_node.val)

            self.res.append("#")
