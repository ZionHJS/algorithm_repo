class Solution:
    def __init__(self):
        self.min_res = []
        self.leafsum = 0

    def mctFromLeafValues(self, arr: List[int]) -> int:

    def leaf_sum(self, root):
        if not root:
            return
        if not root.left and not root.right:
            leafval = root.val
            return leafval

        leaf_sum_left = leaf_sum(root.left)
        leaf_sum_right = leaf_sum(root.right)

        leaf_sum = leaf_sum_left + leaf_sum_right
        return leaf_sum
