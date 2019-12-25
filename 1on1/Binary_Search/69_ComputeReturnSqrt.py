LeetCode 69


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left, right = 0, x

        while left + 1 < right:
            mid = left + (right - left) // 2
            if mid * mid == x:
                return mid
            if mid * mid < x:
                left = mid
            else:
                right = mid
        if right * right < x:
            return right
        return left
