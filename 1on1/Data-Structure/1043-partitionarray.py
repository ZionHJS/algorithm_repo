from collections import deque


class Solution:
    def __init__(self):
        self.res = []

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        elif len(A) <= K:
            return max(A)*len(A)

        times, remainder = divmod(len(A), K)
        A.sort()
        dq = deque()
        for num in A:
            dq.append(num)

        for t in range(times+1):
            max_num = dq.pop()
            self.res.append([max_num])

        while len(dq) > 0:
            for i in range(K-1):
                dq.popleft()
                self.res[times].append(self.res[times][0])
            times -= 1
