class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        bt = TreeNode(-math.inf)
        tp = TreeNode(math.inf)

        def check(root, bt, tp):
            if not root:
                return None
            if root.val < bt.val:
                bt.val, root.val = root.val, bt.val
                return bt
            elif root.val > tp.val:
                tp.val, root.val = root.val, tp.val
                return tp
            if root.left:
                left_res = check(root.left, bt, root)
                if left_res:
                    return left_res
            if root.right:
                right_res = check(root.right, root, tp)
                if right_res:
                    return right_res
            return None
        tmp_res = check(root, bt, tp)
        while tmp_res:
            tmp_res = check(root, bt, tp)
        if root.left:
            self.recoverTree(root.left)
        if root.right:
            self.recoverTree(root.right)
