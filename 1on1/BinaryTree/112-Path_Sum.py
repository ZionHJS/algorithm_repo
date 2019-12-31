# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif not root.left and not root.right and root.val == sum:  # conquer
            return True

        # return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum - root.val)  #divide
        sum_left = self.hasPathSum(root.left, sum - root.val)
        sum_right = self.hasPathSum(root.right, sum - root.val)

        if sum_left or sum_right:
            return True
        else:
            return False


print(0 == False)
