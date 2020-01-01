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
        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        root = TreeNode(None)
        self.helper(root, preorder, inorder)
        return root

    def helper(self, root, preorder, inorder):
        if not root:
            return

        root.val = preorder[0]
        # preorder.remove(root.root.val)
        root_index_in = inorder.index(root.val)

        self.helper(
            root.left, preorder[:root_index_in], inorder[:root_index_in])
        self.helper(
            root.right, preorder[:root_index_in], inorder[:root_index_in])
