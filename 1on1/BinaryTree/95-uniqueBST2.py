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
            root = TreeNode(n)
            return [root]
        else:
            self.nlist = [x for x in range(1, n+1)]
            self.treeHelper(nlist):

    def treeHelper(self, list):
        if not list:
            return None
        if len(list) == 1:
            return TreeNode(list[0])
        else:
            for i in range(1, len(list)+1):
                root = TreeNode(i)
                root.left = self.treeHelper(list[:i])
                root.right = self.treeHelper(list[i+1:])
