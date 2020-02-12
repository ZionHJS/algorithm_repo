# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.temp_node = TreeNode(0)

    def flatten(self, root: TreeNode) -> None:
        if not root.left and not root.right:
            return root
        elif not root:
            return None

        cur_node = TreeNode(0)

        self.traver_helper(root, cur_node)

        print("cur_node_right:", cur_node.right)
        return cur_node.right

    def traver_helper(self, root, cur_node):
        if not root:
            self.temp_node = cur_node
            return

        cur_node.right = TreeNode(root.val)

        self.traver_helper(root.left, cur_node.right)
        self.traver_helper(root.right, self.temp_node)
