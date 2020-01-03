import heapq


class Solution(object):
    def kClosest(self, points, K):
        if not points:
            return []

        dic = {}

        for i in points:
            dis_i = self.get_dis(points[i])

    def get_dis(self, point):
        return sqrt(pow(point[0], 2) + pow(point[1], 2))
