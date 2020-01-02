# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return

        if len(nums) == 1:
            return TreeNode(nums[0])

        mid = len(nums)//2
        root = TreeNode(nums[mid])

        root.left = self.addNodes(nums[0:mid])
        root.right = self.addNodes(nums[mid+1:])

        return root

    def addNodes(self, nums):
        if not nums:
            return

        if len(nums) == 1:
            return TreeNode(nums[0])

        # when len(nums) >= 2
        mid = len(nums)//2
        root = TreeNode(nums[mid])

        root.left = self.addNodes(nums[0:mid])
        root.right = None

        return root
