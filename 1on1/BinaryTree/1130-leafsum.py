class Solution:
    def __init__(self):
        self.min_res = []

    def mctFromLeafValues(self, arr: List[int]) -> int:
        if len(arr) < 2:  # never gonna happen
            return None

        for i in range(0, len(arr) - 1):  # when len > = 2 and len must >= 2
            root = TreeNode(max(arr[0:i+1])*max(arr[i+1:]))
            root.left = self.nodefromlist(arr[0:i+1])  # len must >= 1
            root.right = self.nodefromlist(arr[i+1:])  # len must >= 1

            self.min_res.append(self.non_leaf_sum(root, 0))

        return min(self.min_res)

    def nodefromlist(self, list):
        print(list)
        if len(list) == 0:
            return None
        elif len(list) == 1:
            return TreeNode(list[0])
        else:
            # when len(list) >= 2
            for j in range(0, len(list) - 1):
                root = TreeNode(max(list[0:j+1])*max(list[j+1:]))
                root.left = self.nodefromlist(list[0:j+1])
                root.right = self.nodefromlist(list[j+1:])

    def non_leaf_sum(self, root, nonleafsum):
        if not root:
            return nonleafsum
        if not root.left and not root.right:  # end condition
            return nonleafsum
        else:
            non_leaf_sum_left = self.non_leaf_sum(
                root.left, nonleafsum + root.val)
            non_leaf_sum_right = self.non_leaf_sum(
                root.right, nonleafsum + root.val)

            return non_leaf_sum_left + non_leaf_sum_right


list_a = [0, 1, 2, 3, 4, 5, 6]
a = list_a[6:]
b = list_a[0:0]
c = list_a[0:1]
print(a)
print(b)
print(c)
