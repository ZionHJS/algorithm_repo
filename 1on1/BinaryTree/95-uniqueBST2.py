# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def generateTrees(self, n):
        if n < 1:
            return []
        if n == 1:
            return [TreeNode(1)]
        else:
            self.nlist = [i for i in range(1, n+1)]

            return self.treeHelper(self.nlist)

    def treeHelper(self, list):
        res = []
        if not list:
            return [None]
        if len(list) == 1:
            return [TreeNode(list[0])]
        else:
            for i in range(0, len(list)):  # index
                for l in self.treeHelper(list[:i]):
                    for r in self.treeHelper(list[i+1:]):
                        root = TreeNode(list[i])
                        root.left = l
                        root.right = r

                        res.append(root)

            return res
