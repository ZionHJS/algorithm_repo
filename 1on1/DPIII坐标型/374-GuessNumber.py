# The guess API is already defined for you.
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        if n == 1:
            return n

        left, right = 1, n

        while left+1 < right:
            mid = left+(right-left)//2

            if guess(mid) == 0:
                return mid
            elif guess(mid) > 0:
                right = mid
            else:
                left = mid

        if guess(right) > 0:
            return left
        else:
            return right
