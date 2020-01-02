# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.left_list = []
        self.right_list = []

    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return None
        elif not root.left and not root.right:
            return True
        elif root.left and root.right:
            self.replaceroot(root.right)
            self.preorder(root.left, self.left_list)
            self.preorder(root.right, self.right_list)
            for i in range(len(self.left_list)):
                if self.left_list[i] != self.right_list[i]:
                    return False
            return True
        else:
            return False

    def replaceroot(self, root):
        if not root:
            return
        else:
            tmp_root = root.left
            root.left = root.right
            root.right = tmp_root

            self.replaceroot(root.left)
            self.replaceroot(root.right)

    def preorder(self, root, list):
        if not root:
            return

        list.append(root.val)
        self.preorder(root.left, list)
        self.preorder(root.right, list)
