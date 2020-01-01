class Solution:
    def __init__(self):
        self.min_res = []

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) < 2:  # never gonna happen
            return None

        for i in range(0, len(arr) - 1):  # when len > = 2 and len must >= 2
            root = TreeNode(max(arr[0:i+1]) + max(arr[i+1:]))
            root.left = self.nodefromlist(arr[0:i+1])  # len must >= 1
            root.right = self.nodefromlist(arr[i+1:])  # len must >= 1

            self.min_res.append(self.non_leaf_sum(root, 0))

        return min(self.min_res)

    def nodefromlist(self, list):
        if len(list) == 0:
            return None
        elif len(list) == 1:
            return TreeNode(list[0])

        for j in range(0, len(list) - 1):  # len must >= 2
            root = TreeNode(max(list[0:j+1]) + max(list[j+1:]))
            root.left = self.nodefromlist(max(list[0:j+1]))
            root.right = self.nodefromlist(max(list[j+1:]))

    def non_leaf_sum(self, root, nonleafsum):
        if not root:
            return 0
        if not root.left and not root.right:
            return nonleafsum
        else:
            nonleafsum += root.val

        non_leaf_sum_left = leaf_sum(root.left, nonleafsum)
        non_leaf_sum_right = leaf_sum(root.right, nonleafsum)

        non_leaf_sum = non_leaf_sum_left + non_leaf_sum_right
        return non_leaf_sum


list_a = [0, 1, 2, 3, 4, 5, 6]
a = list_a[6:]
b = list_a[0:0]
c = list_a[0:1]
print(a)
print(b)
print(c)
