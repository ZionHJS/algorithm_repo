import heapq


class Solution(object):
    def kClosest(self, points, K):
        if not points:
            return []

        dic = {}
        heap = []

        for i in points:
            dis_i = self.get_dis(points[i])
            if dis_i not in dic:
                dic[dis_i] = []
            dic[dis_i].append(points[i])  # zipper

        for j in range(k):
            for m in dic:
                heapq.heappush(heap, m)

        return heapq.heappop(heap)

    def get_dis(self, point):
        return sqrt(pow(point[0], 2) + pow(point[1], 2))
