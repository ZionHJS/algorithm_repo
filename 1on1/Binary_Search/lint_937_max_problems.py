import math


class Solution:
    """
    @param n: an integer
    @param k: an integer
    @return: how many problem can you accept
    """

    def canAccept(self, n, k):
        if not n:
            return -1

        left, right = 0, math.sqrt(2*n)
        ans = 0

        while left + 1 < right:
            mid = left+(right-left)//2
            if self.pro_nums(mid, k) <= n:
                ans = mid
                left = mid
            else:
                right = mid

        if self.pro_nums(right, k) <= n:
            ans = right
        else:
            ans = left
        return ans

    def pro_nums(self, m, k):
        total = 0
        for i in range(1, m+1):
            total += k*i
        return total
