import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1 or n == 2:
            return n

        base = [2, 3, 5]
        heap = []

        for i in range(0, 4):
            self.getMultiply(base, i, 1, n)  # i => 1,2,3

        return heap[0]

    def getMultiply(self, base, times, multi, n):
        if times == 0:
            if len(heap) < n:
                heapq.heappush(heap, -multi)
            else:
                if multi > -heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, -multi)
            return

        for i in range(1, len(base)):
            multi *= base[i]
            self.getMultiply(base[1:], times-1, multi, n)

        return
