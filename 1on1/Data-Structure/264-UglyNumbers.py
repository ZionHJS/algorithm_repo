import heapq
import queue


class Solution:
    def __init__(self):
        self.heap = []

    def nthUglyNumber(self, n: int) -> int:
        if n <= 6:
            return n

        factors = [2, 3, 5]
        q = queue.Queue()
        q.put(1)
        heapq.heappush(self.heap, -1)  # initialization

        # bfs
        while q.qsize():
            for i in range(q.qsize()):
                cur_multi = q.get()
                for factor in factors:
                    if len(self.heap) < n:
                        if -cur_multi*factor not in self.heap:
                            heapq.heappush(self.heap, -cur_multi*factor)
                            q.put(cur_multi*factor)
                    else:
                        if -cur_multi*factor not in self.heap:
                            if cur_multi*factor < -self.heap[0]:
                                heapq.heappop(self.heap)
                                heapq.heappush(self.heap, -cur_multi*factor)

        return -self.heap[0]
