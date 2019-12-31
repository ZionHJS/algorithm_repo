# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import copy


class Solution:
    def __init__(self):
        self.res = []

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:
            return []

        self.helper(root, sum, [])
        return self.res

    def helper(self, root, sum, list):
        dep_list = copy.deepcopy(list)
        # list.clear()
        if not root:
            return
        else:
            dep_list.append(root.val)

        if not root.left and not root.right:
            if root.val == sum:
                self.res.append(dep_list)

            return

        self.helper(root.left, sum-root.val, dep_list)
        self.helper(root.right, sum-root.val, dep_list)
