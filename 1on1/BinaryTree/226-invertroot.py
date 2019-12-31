class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return
        if not root.left and not root.right:
            return root

        left_node = self.invertTree(root.right)
        right_node = self.invertTree(root.left)

        root.left = left_node
        root.right = right_node
        return root
