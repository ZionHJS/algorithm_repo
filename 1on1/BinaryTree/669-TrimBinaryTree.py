# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        if root.val < L:
            root = root.right
            print("root:", root)
            return self.trimBST(root, L, R)
        elif root.val > R:
            root = root.left
            print("root:", root)
            return self.trimBST(root, L, R)

        return self.inorder_traver(root, L, R)

    def inorder_traver(self, root, L, R):
        if not root:
            return None
        elif root.val < L:
            root = root.right
            return self.inorder_traver(root, L, R)
        elif root.val > R:
            root = root.left
            return self.inorder_traver(root, L, R)

        left = self.inorder_traver(root.left, L, R)
        right = self.inorder_traver(root.right, L, R)

        root.left = left
        root.right = right

        return root
