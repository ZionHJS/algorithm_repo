import heapq
#print("heapify:", heapq.heapify([2, 3, 6, 1, 0, -1]))
print("heapify:", heapq.heapify([2, 3, 4, 5, 6]))


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


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums_ = nums[-5:]
#print("nums_:", nums_)
print("heapify:", heapq.heapify([2, 3, 6, 1, 0, -1]))
