class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        target = Y
        dis = 0

        while target > X:
            if not target % 2:
                target = target + 1
                dis += 1
            target //= 2
            dis += 1

        return dis+X-target
