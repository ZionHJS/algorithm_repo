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

        #root = TreeNode(preorder[0])
        self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        if len(inorder) == 1 or len(preorder) == 0:
            return None
        else:
            val = preorder[0]
            root = TreeNode(val)
            root_index_pre = preorder.index(val)
            root_index_in = inorder.index(val)

        root.left = self.helper(
            preorder[root_index_pre+1:], inorder[:root_index_in])  # range correct
        root.right = self.helper(
            preorder[root_index_pre+root_index_in+1:], inorder[root_index_in+1:])  # range correct

        return root
