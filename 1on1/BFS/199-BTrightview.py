# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue


class Solution:
    def __init__(self):
        self.level = []
        self.res = []

    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        elif not root.left and not root.right:
            return [root.val]

        q = queue.Queue()
        q.put(root)
        while q.qsize():
            n = q.qsize()
            for i in range(n):
                cur_node = q.get()
                if cur_node.left:
                    q.put(cur_node.left)
                if cur_node.right:
                    q.put(cur_node.right)
                self.level.append(cur_node.val)

            self.res.append(self.level.pop())

        return self.res
