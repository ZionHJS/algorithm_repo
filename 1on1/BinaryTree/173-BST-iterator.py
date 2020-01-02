# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.root = root
        self.cur_root = root
        self.pre_root = root
        self.res = 0

    def next(self) -> int:
        if not self.cur_root:
            self.cur_root = self.root.right
            self.res = self.root.val
            self.root = None
            return self.res

        if self.cur_root.left and self.cur_root.right:
            self.cur_root = self.cur_root.left
            self.pre_root = self.cur_root
            self.next()
        elif not self.cur_root.left and self.cur_root.right:
            self.cur_root = self.cur_root.right
            self.res = self.cur_root.val
            self.cur_root.val = None
            return self.res
        else:
            self.res = self.cur_root.val
            self.cur_root.val = None
            self.cur_root = self.pre_root
            return self.res

    def hasNext(self) -> bool:
        if self.next():
            return True
        else:
            return False
