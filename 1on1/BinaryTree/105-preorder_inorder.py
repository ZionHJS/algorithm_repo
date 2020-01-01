# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        elif len(preorder) == 1 and len(inorder) == 1:
            return TreeNode(preorder[0])

        self.helper([] + preorder, [] + inorder)

    def helper(self, preoder, inorder):
        if not preorder:
            return

        preorder.remove(root.val)

        root.left = helper([] + preorder, [] + inorder)
        root.right = helper([] + preorder, [] + inorder)
