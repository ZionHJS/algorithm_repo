# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.tree_depth = 0
        self.unfilled = 0

    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif not root.left or not root.right:
            return 2

        self.depth_helper(root, 0)

        return 2**(self.tree_depth+1)-1-self.unfilled

    def depth_helper(self, root, cur_depth):  # cur_depth  begin => 0
        if not root:
            self.tree_depth = max(self.tree_depth, cur_depth)
            return
        elif (root.left and not root.right) or (root.right and not root.left):
            self.tree_depth = max(self.tree_depth, cur_depth+1)
            self.unfilled += 1
            return

        cur_depth += 1

        self.depth_helper(root.left, cur_depth)
        self.depth_helper(root.right, cur_depth)
