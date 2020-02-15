import math
import queue


class Solution:
    def __init__(self):
        self.level_n = 1

    def numSquares(self, n: int) -> int:
        if n <= 1:
            return n

        sqrt_n = math.floor(math.sqrt(n))
        #print("sqrt_n:", sqrt_n)
        #set_A = set()
        q_A = queue.Queue()
        q_A.put(n)
        # set_A.add(n)
        set_B = set()
        dis = 0
        for i in range(1, sqrt_n+1):
            set_B.add(i**2)

        # bfs
        while q_A.qsize() > 0:
            dis += 1
            cur_level_n = 0

            for i in range(self.level_n):
                cur_n = q_A.get()
                for num in set_B:
                    if cur_n - num > 0:
                        q_A.put(cur_n - num)
                        cur_level_n += 1
                    elif cur_n - num == 0:
                        return dis

            self.leve_n = cur_level_n

        return 0
