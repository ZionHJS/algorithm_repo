class Solution:
    def __init__(self):
        self.res = []
        self.sum = 0

    def numTrees(self, n: int) -> int:
        if n < 2:
            return 0

        for i in range(1, n+1):  # root-range: 1 ~ n
            left_count = self.count_bst(i-1)
            right_count = self.count_bst(n-i)

            sum_count = left_count*right_count
            self.sum += sum_count

        return self.sum

    def count_bst(self, n):
        if n == 0:
            return 0
        if n == 1:
            return 1

        for j in range(1, n+1):
            left_count = self.count_bst(i-1)
            right_count = self.count_bst(n-i)

            return left_count + right_count
