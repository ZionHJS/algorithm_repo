class Solution(object):
    def myPow(self, x, n):
        if not x:
            return 0
        elif not n:
            return 1

        result = 1

        if n > 0:
            for i in range(1, n+1):
                result = result*x
            return result
        else:
            for i in range(1, abs(n)+1):
                result = result*x
            return 1/result
