# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.count = 0

    def pathSum(self, root: TreeNode, sum: int) -> int:
        origin_sum = sum

        def helper(root, sum):
            if not root:
                return

            if root.val == sum:
                self.count += 1

            if root.left:
                helper(root.left, sum-root.val)
                helper(root.left, origin_sum)
            if root.right:
                helper(root.right, sum-root.val)
                helper(root.right, origin_sum)

        helper(root, sum)

        return self.count
