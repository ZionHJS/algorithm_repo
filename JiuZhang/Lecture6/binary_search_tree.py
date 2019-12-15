# coding=utf-8

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.__root = None   #创建一个空的BST树函数 开始往里面增加节点

    def add(self, val):
        self.__root = self.__add_helper(self.__root, val)

    def __add_helper(self, root, val):
        if not root:   #root 为 null时  Exit Condition call back
            return TreeNode(val)
        if val < root.val:
            root.left = self.__add_helper(root.left, val)
        else:
            root.right = self.__add_helper(root.right, val)
        return root   #end call back 

    def contains(self, val):
        return self.__contains_helper(self.__root, val)

    def __contains_helper(self, root, val):
        if not root:   #exit condition callback False
            return False

        if root.val == val:
            return True   #exit condition callback True
        elif val < root.val:
            return self.__contains_helper(root.left, val)
        else:
            return self.__contains_helper(root.right, val)

bst = BST()
bst.add(10)
bst.add(11)
bst.add(9)

print(bst)

print(bst.contains(10))
print(bst.contains(11))
print(bst.contains(9))

print(bst.contains(8))
