from collections import deque


class Solution:
    def __init__(self):
        self.res = []
        self.sum = 0

    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        if not A:
            return 0
        elif len(A) <= K:
            return max(A)*len(A)

        times, remainder = divmod(len(A), K)
        A.sort()
        cur_idx = len(A)-1
        print("A_sorted:", A)
        #print("times:", times)
        #print("remainder:", remainder)

        for t in range(times):
            while A[cur_idx] == self.res[-1]:
                cur_idx -= 1
            max_num = A[cur_idx]
            cur_idx -= 1
            self.res.append(max_num)
            self.sum += max_num

        if remainder:
            while a[cur_idx] == self.res[-1]:
                cur_idx -= 1
            max_num = A[cur_idx]
            cur_idx -= 1
            self.res.append(max_num)
            self.sum += max_num

        self.res.sort()
        print("sum_begin:", self.sum)

        bfs
        dq = deque()
        for num in A:
            dq.append(num)

        while len(dq) > 0:
            for i in range(1, K):
                if len(dq) > 0:
                    dq.popleft()
                    # self.res[times].append(self.res[times])
                    self.sum += self.res[times]
                    #print("sum_now:", self.sum)
            times -= 1

        return self.sum
