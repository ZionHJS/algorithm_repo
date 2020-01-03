# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.nlist = []
        self.res = []

    def generateTrees(self, n: int) -> List[TreeNode]:
        if n < 1:
            return []
        if n == 1:
            return [TreeNode(1)]
        else:
            self.nlist = [x for x in range(1, n+1)]
            self.treeHelper(self.nlist)

            return self.res

    def treeHelper(self, list):
        if not list:
            return [None]
        if len(list) == 1:
            return [TreeNode(list[0])]
        else:
            for i in range(0, len(list)):  # index
                for left in self.treeHelper(list[:i]):
                    for right in self.treeHelper(list[i+1:]):
                        root = TreeNode(list[i])
                        root.left = left
                        root.right = right
                        self.res.append(root)
