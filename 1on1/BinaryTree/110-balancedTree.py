# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isBalanced(self, root):
        if not root:
            return True
        elif not root.left and not root.right:
            return True

        return self.height_helper(root, 0)

    def height_helper(self, root, height):
        if not root:
            return height - 1

        height_left = self.height_helper(root.left, height + 1)
        height_right = self.height_helper(root.right, height + 1)

        if not type(height_left) == int or not type(height_right) == int:
            return False
        elif abs(height_left - height_right) > 1:
            return False
        else:
            return max(height_left, height_right)
