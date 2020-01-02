# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.tmp_list = []

    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None

        max_num = max(nums)
        max_index = nums.index(max_num)

        root = TreeNode(max(nums))

        root.left = constructMaximumBinaryTree(nums[:max_index])
        root.right = constructMaximumBinaryTree(nums[max_index+1:])

        return root


list = [0, 1, 2, 3, 4, 5, 6]
list_a = list[:0]
list_b = list[:1]
list_c = list[6:]
list_d = list[5:]
list_f = list[7:]
print(list_a)
print(list_b)
print(list_c)
print(list_d)
print(list_f)
