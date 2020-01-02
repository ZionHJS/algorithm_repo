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
        self.pre_list = []
        self.res = root.val

    def next(self) -> int:
        if not self.cur_root.val:  # only right-leaf return will trigger this
            self.cur_root = self.root
            self.next()

        if self.cur_root.left and self.cur_root.right or self.cur_root.left:
            self.pre_root = self.cur_root
            self.pre_list.append(self.pre_root)
            self.cur_root = self.cur_root.left
            self.next()
        elif self.cur_root.right:
            # self.pre_root = self.cur_root  #block this keep the pre_cur = closest cur_root left-parent
            self.cur_root = self.cur_root.right

            if self.pre_root.val:
                self.res = self.pre_root.val
                self.pre_root.val = None  # right step
                return self.res
            else:
                self.next()
        else:
            print(self.cur_root.val)
            if self.pre_root.left:  # cut left first and then cut right
                self.pre_root.left = None
            else:
                self.pre_root.right = None

            if not self.cur_root.val:
                self.cur_root = self.pre_root
                self.next()
            else:
                self.res = self.cur_root.val
                self.cur_root = self.pre_root
                return self.res

    def hasNext(self) -> bool:
        if not self.next():
            return False
        else:
            return True


test_list = [0, 1, 2, 3, 4, 5, None, None, None, None]
test_list.remove(None)
print(test_list)
