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
            self.pre_list = [x for x in self.pre_list if x.val != None]
            print(self.pre_list)
            self.cur_root = self.pre_list.pop()
            self.next()

        if self.cur_root.left and self.cur_root.right or self.cur_root.left:
            self.pre_root = self.cur_root
            self.pre_list.append(self.pre_root)

            self.cur_root = self.cur_root.left
            self.next()
        elif self.cur_root.right:
            self.pre_root = self.cur_root
            self.pre_list.append(self.pre_root)

            self.res = self.cur_root.val
            self.cur_root.val = None  # right step
            self.cur_root = self.cur_root.right
            return self.res
        else:
            if self.pre_root.left:  # cut left first and then cut right
                self.pre_root.left = None
            else:
                self.pre_root.right = None

            self.res = self.cur_root.val
            self.cur_root = self.pre_list.pop()
            return self.res

    def hasNext(self) -> bool:
        if not self.next():
            return False
        else:
            return True
