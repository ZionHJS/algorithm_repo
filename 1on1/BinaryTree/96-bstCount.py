class Solution:
    def __init__(self):
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

    def count_bst(self, n):  # numbers of left-side
        if m <= 1:
            return 1
        else:
            # when i >= 2
            for j in range(1, n+1):
                left_count = self.count_bst(j-1)
                right_count = self.count_bst(n-j)

                return left_count*right_count
