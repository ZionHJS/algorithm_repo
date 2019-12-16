#2  判断一颗二叉树是否左右平衡
# Defination of TreeNode
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None

class Solution:
    # @param root:The rootof binary Tree
    # @return: True if this Binary tree is Balanced, or False 
    def isBalanced(self, root):
        if not root:
            return True
        if not isBalanced(root.left):
            return False
        if not isBalanced(root.right):
            return False
        
        return abs(self.get_height(root.left)-self.get_height(root.right)) <= 1

    def get_height(self, root):
        #分治
        if not root:
            return 0
        #因为所有树高度是左子树高度和右子树高度的最大值加1
        return max(self.get_height(root.left), self.get_height(root.right)) + 1

#3 判断一棵树是否是合法的BST
Definition of TreeNode:
# class TreeNode:
#     def __init__(self, val):
#         self.val = val
#         self.left, self.right = None, None

class Solution:
    # @param root: The root of binary tree
    # @return True is the binary tress is BST, or false
    def isValidBST(self, root):
        return self.helper(root, float('-inf'), float('inf'))
    
    def helper(self, root, min_value, max_value):
        if not root:
            return True
        if root.val <= min_value:
            return False
        if root.val >= max_value:
            return False

        return self.helper(root.left, min_value, root.val) and self.helper(root.right, root.val, max_value)

