# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return None
        elif not root.left and not root.right:
            return True
        elif root.left and root.right:
            self.replaceroot(root.right)
            return self.issametree(root.left, root.right)
        else:
            return False

    def replaceroot(self, root):
        if not root:
            return
        else:
            tmp_root = root.left
            root.left = root.right
            root.right = tmp_root

            self.replaceroot(root.left)
            self.replaceroot(root.right)

    def issametree(self, p, q):
        if not p and not q:
            return True

        if p != q:
            return False
        elif p == q:
            left_bool = self.issametree(p.left, q.left)
            right_bool = self.issametree(p.right, q.right)
            if left_bool and right_boll:
                return True
            else:
                return False
