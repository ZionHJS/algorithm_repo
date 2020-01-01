# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1 and not t2:
            return None
        elif t1 and t2:
            t3 = TreeNode(t1.val + t2.val)
        else:
            if not t2:
                t3 = TreeNode(t1.val)
            else:
                t3 = TreeNode(t2.val)

        if t1 and t2:
            t3.left = self.mergeTrees(t1.left, t2.left)
            t3.right = self.mergeTrees(t1.right, t2.right)
        else:
            if not t1:
                t3.left = self.mergeTrees(None, t2.left)
                t3.right = self.mergeTrees(None, t2.right)
            else:
                t3.left = self.mergeTrees(t1.left, None)
                t3.right = self.mergeTrees(t1.right, None)

        return t3
