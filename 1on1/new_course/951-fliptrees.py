# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        elif root1.val != root2.val:
            return False

        # single child-node
        if not root1.left and not root2.left:
            return self.flipEquiv(root1.right, root2.right)
        elif not root1.right and not root2.right:
            return self.flipEquiv(root1.left, root2.left)
        elif not root1.left and not root2.right:
            return self.flipEquiv(root1.right, root2.left)
        else:
            return self.flipEquiv(root1.left, root2.right)

        # double child-node
        if root1.left < root1.right:
            if root2.left < root2.right:
                left_bool = self.flipEquiv(root1.left, root2.left)
                right_bool = self.flipEquiv(root1.right, root2.right)
            else:
                left_bool = self.flipEquiv(root1.left, root2.right)
                right_bool = self.flipEquiv(root1, right, root2.left)
        else:
            if root2.left > root2.right:
                left_bool = self.flipEquiv(root1.right, root2.right)
                right_bool = self.flipEquiv(root1.left, root2.left)
            else:
                left_bool = self.flipEquiv(root1.right, root2.left)
                right_bool = self.flipEquiv(root1.left, root2.right)

        print("left:", left_bool, "right:", right_bool)
        return left_bool and right_bool
