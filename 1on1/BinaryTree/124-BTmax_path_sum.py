# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.max_sum = 0
        self.sum_dic = {}

    def maxPathSum(self, root: TreeNode) -> int:
        self.pre_helper(root)

        return self.max_sum

    def pre_helper(self, root):
        if not root:
            return 0

        if root.left in self.sum_dic:
            left_sum = self.sum_dic[root.left]
        else:
            left_sum = self.max_node_sum(root.left, root.val)

        if root.right in self.sum_dic:
            right_sum = self.sum_dic[root.right]
        else:
            right_sum = self.max_node_sum(root.right, root.val)

        max_cur_sum = max(left_sum+root.val, right_sum +
                          root.val, left_sum+right_sum+root.val)

        self.max_sum = max(self.max_sum, max_cur_sum)  # post order

        self.pre_helper(root.left)
        self.pre_helper(root.right)

    def max_node_sum(self, root, pre_sum):
        if not root:
            return pre_sum

        temp_sum = pre_sum
        pre_sum += root.val

        left_sum = self.max_node_sum(root.left, pre_sum)
        right_sum = self.max_node_sum(root.right, pre_sum)

        max_cur_sum = max(left_sum, right_sum, left_sum+right_sum-pre_sum)

        self.sum_dic[root] = max_cur_sum - temp_sum
        return max_cur_sum
