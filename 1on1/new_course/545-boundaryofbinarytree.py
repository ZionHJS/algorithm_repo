class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if not root or not root.left or not root.right:
            return root

        self.res = []
        self.res.append(root)
        if root.left:
            self.find_boundary(root.left, True)
            if root.right:
                self.find_boundary(root.right, False)
        elif root.right:
            self.find_boundary(root.right, True)

        return self.res

    def find_boundary(self, root, boolean):
        if not root:
            return
        if boolean == True or (not root.left or not root.right):
            self.res.append(root)

        if root.left:
            if boolean:
                self.find_boundary(root.left, True)
                if root.right:
                    self.find_boundary(root.right, False)
            else:
                self.find_boundary(root.left, False)
                if root.right:
                    self.find_boundary(root.right, False)
        elif root.right:
            if boolean:
                self.find_boundary(root.right, True)
            else:
                self.find_boundary(root.right, False)
