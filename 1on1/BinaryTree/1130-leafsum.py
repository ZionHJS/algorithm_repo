class Solution:
    def __init__(self):
        self.min_res = []

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(list) < 2:
            return False

        for i in range(1, len(list)-1):
            self.treefrom2list(list[0:i], list[i:len(list)-1])

    def treefrom2list(self, list1, list2):
        if not list1 or not list2:
            return None

        root = TreeNode(max(list1) + max(list2))

        for m in range(1, len(list1)-1):
            root.left = treefrom2list(list1[0:m], list[m:len(list1)-1])
            for k in range(1, len(list2)-1):
                root.left = treefrom2list(list2[0:k], list[k:len(list2)-1])
            self.min_res.append(root.val)
            return root

    def non_leaf_sum(self, root, nonleafsum):
        if not root:
            return 0
        if not root.left and not root.right:
            return 0
        else:
            nonleafsum += root.val

        non_leaf_sum_left = leaf_sum(root.left, nonleafsum)
        non_leaf_sum_right = leaf_sum(root.right, nonleafsum)

        non_leaf_sum = non_leaf_sum_left + non_leaf_sum_right
        return non_leaf_sum


class Solution:
    def __init__(self):
        self.min_res = []

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(list) < 2:
            return False

        for i in range(0, len(list)-1):
            self.treefrom2list(list[0:i+1], list[i+1:])

    def treefrom2list(self, list1, list2):
        if not list1 or not list2:
            return None

        root = TreeNode(max(list1) + max(list2))

        for m in range(0, len(list1)-1):
            root.left = treefrom2list(list1[0:m+1], list1[m+1:])
            for k in range(1, len(list2)-1):
                root.right = treefrom2list(list2[0:k+1], list2[k+1:])
