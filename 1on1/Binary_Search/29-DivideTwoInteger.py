import math


class Solution(object):
    def divide(self, dividend, divisor):
        if dividend == 0:
            return 0
        elif dividend / divisor > math.pow(2, 31) - 1:
            return int(math.pow(2, 31) - 1)
        elif dividend / divisor < math.pow(-2, 31):
            return int(math.pow(-2, 31))

        elif dividend*divisor > 0:
            left, right = 0, abs(dividend)
            while left + 1 < right:
                mid = left + (right-left)//2
                if mid*abs(divisor) == abs(dividend):
                    return mid
                elif mid*abs(divisor) > abs(dividend):
                    right = mid
                else:
                    left = mid

            if right*abs(divisor) <= abs(dividend):
                return int(right)
            else:
                return int(left)
        else:
            left, right = 0, abs(dividend)
            while left + 1 < right:
                mid = left + (right-left)//2
                if mid*abs(divisor) == abs(dividend):
                    return mid
                elif mid*abs(divisor) > abs(dividend):
                    right = mid
                else:
                    left = mid

            if right*abs(divisor) <= abs(dividend):
                return int(0 - right)
            else:
                return int(0 - left)

        return -1
