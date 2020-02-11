# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def __init__(self):
        self.max_sum = -1e8  # -1e8 就是一个很大很大的数
        self.sum_dic = {}

    def maxPathSum(self, root: TreeNode) -> int:
        self.pre_helper(root)
        return self.max_sum

    def pre_helper(self, root):
        if not root:
            return

        if root.left not in self.sum_dic:
            left_max_sum = self.max_node_sum(root.left, root.val)
        else:
            left_max_sum = self.sum_dic[root.left] + root.val

        if root.right not in self.sum_dic:
            right_max_sum = self.max_node_sum(root.right, root.val)
        else:
            right_max_sum = self.sum_dic[root.right] + root.val

        cur_max_sum = max(root.val, left_max_sum, right_max_sum,
                          left_max_sum+right_max_sum-root.val)

        self.max_sum = max(self.max_sum, cur_max_sum)  # pre-order

        self.pre_helper(root.left)
        self.pre_helper(root.right)

    def max_node_sum(self, root, pre_sum):
        if not root:
            return pre_sum

        temp_sum = pre_sum
        pre_sum += root.val

        left_sum = self.max_node_sum(root.left, pre_sum)
        right_sum = self.max_node_sum(root.right, pre_sum)

        #max_cur_sum = max(left_sum, right_sum, left_sum+right_sum-pre_sum)
        max_cur_sum = max(pre_sum, left_sum, right_sum)

        self.sum_dic[root] = max_cur_sum - temp_sum
        return max_cur_sum
