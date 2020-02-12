import heapq


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        for i in range(len(nums)):
            if len(self.heap) < k:
                heapq.heappush(self.heap, nums[i])
            else:
                if nums[i] > self.heap[0]:
                    heapq.heappop(self.heap)
                    heapq.heappush(self.heap, nums[i])

    def add(self, val: int) -> int:
        if val > self.heap[0]:
            heapq.heappush(self.heap, val)
            return heapq.heappop(self.heap)
        else:
            return heapq.heappop(self.heap)
