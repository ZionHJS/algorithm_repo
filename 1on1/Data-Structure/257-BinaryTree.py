# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.res = []
        self.arrow = "->"

    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        temp_path = ""

    def dfs(self, root, temp_path):
        if not root.left and not root.right:
            temp_path = temp_path + self.arrow + root.val
            self.res.append(temp_path)

        if root.left:
            self.dfs(root.left, temp_path)
        if root.rigt:
            self.dfs(root.right, temp_path)
