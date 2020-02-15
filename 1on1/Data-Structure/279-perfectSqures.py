import math


class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n

        sqrt_n = math.floor(math.sqrt(n))
        #print("sqrt_n:", sqrt_n)
        set_A = set()
        set_A.add(n)
        set_B = set()
        dis = 0
        for i in range(1, sqrt_n+1):
            set_B.add(i**2)

        # bfs
        while set_A:
            dis += 1
            for num in set_B:
                if num not in set_A:
                    if n - num > 0:
                        set_A.add(n-num)
                    else:
                        continue
                else:
                    return dis

        return 0
