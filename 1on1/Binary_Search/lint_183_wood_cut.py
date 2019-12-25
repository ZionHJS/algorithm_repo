LintCode 183


class Solution:
    """
    @param L: Given n pieces of wood with length L[i]
    @param k: An integer
    @return: The maximum length of the small pieces
    """

    def woodCut(self, L, k):
        # write your code here
        if not L:
            return 0
        ans = 0
        left = 1
        right = max(l for l in L)

        while left + 1 < right:
            mid = left + (right - left) // 2
            if self.getCount(mid, L) >= k:
                ans = mid
                left = mid
            else:
                right = mid
        if self.getCount(left, L) >= k:
            ans = left
        if self.getCount(right, L) >= k:
            ans = right
        return ans

    def getCount(self, mid, L):
        count = 0
        for l in L:
            count += l // mid
        return count
