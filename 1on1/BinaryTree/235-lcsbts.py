# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None

        if root == p or root == q:
            return root

        lcs_left = self.lowestCommonAncestor(root.left, p, q)
        lcs_right = self.lowestCommonAncestor(root.right, p, q)

        if lcs_left and lcs_right:
            return root
        elif lcs_left:
            return lcs_left
        elif lcs_right:
            return lcs_right
        else:
            return None
