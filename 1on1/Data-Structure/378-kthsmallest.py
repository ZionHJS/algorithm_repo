import heapq


class Solution(object):
    def kthSmallest(self, matrix, k):
        if not matrix:
            return None

        heap = []

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(heap) < k:
                    heapq.heappush(heap, -matrix[i][j])
                else:
                    if -matrix[i][j] >= heap[0]:
                        heapq.heappop(heap)
                        heapq.heappush(heap, -matrix[i][j])

        return -heap[0]
