# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        self.helper(root, sum, list)

        return res

    def helper(self, root, sum, list):
        if not root:
            list.clear()
            return
        else:
            list.append(root.val)

        if not root.left and not root.right:
            if root.val = sum:
                res.append(list)
            else:
                list.clear()

        self.helper(root.left, sum-root.val)
        self.helper(root.right, sum-root.val)
