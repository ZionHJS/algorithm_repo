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

        # root = TreeNode(preorder[0])
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


# 简化版本
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder and not inorder:
            return None
        elif len(preorder) == 1:
            return TreeNode(preorder[0])

        # root = TreeNode(preorder[0])
        return self.helper(preorder, inorder)

    def helper(self, preorder, inorder):
        if len(inorder) == 0 or len(preorder) == 0:
            return None
        else:
            root = TreeNode(preorder[0])
            root_index_in = inorder.index(preorder[0]

        root.left=self.helper(
            preorder[1:root_index_in+1], inorder[:root_index_in])  # range correct
        root.right=self.helper(
            preorder[root_index_in+1:], inorder[root_index_in+1:])  # range correct

        return root


# 一毛一样的代码 为什么我的过不了呢

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if len(inorder) == 0:
            return None

        root=TreeNode(preorder[0])

        root_index_in=inorder.index(preorder[0])

        root.left=self.buildTree(
            preorder[1:root_index_in+1], inorder[:root_index_in])
        root.right=self.buildTree(
            preorder[root_index_in+1:], inorder[root_index_in+1:])

        return root
