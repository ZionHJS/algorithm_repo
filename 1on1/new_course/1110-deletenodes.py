# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.res = []

    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return

        self.res.append(root)

        def dfs(root):
            if not root:
                return

            if self.is_to_del(root.left, to_delete):
                next_left = root.left
                root.left = None
                dfs(next_left)
            if self.is_to_del(root.right, to_delete):
                next_right = root.right
                root.right = None
                dfs(next_right)

        dfs(root)

        return self.res

    def is_to_del(self, root, to_delete):
        n = len(to_delete)

        for i in range(n):
            if root.val == to_delete[i]:
                return True

        return False
