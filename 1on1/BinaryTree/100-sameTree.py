# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p or not q:
            return
        elif p.val == q.val and(not p.left and not p.right) and (not q.left and not q.right):
            return True

        if p.val != q.val:
            return False
        else:
            if p.left and q.left:
                self.isSameTree(p.left, q.left)
            elif p.right and q.right:
                self.isSameTree(p.right, q.right)
            else:
                return False
