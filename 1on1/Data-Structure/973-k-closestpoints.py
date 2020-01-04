import heapq
import math


class Solution(object):
    def kClosest(self, points, K):
        heap = []
        def distance(x): return points[x][0]**2 + points[x][1]**2
        length = len(points)
        for i in range(length):
            heapq.heappush(heap, (distance(i), points[i]))
        res = []
        for i in range(K):
            res.append(heapq.heappop(heap)[1])
        return res


list = [1, 2, 3, 4, 5, 6, 7]
semester = [[], [], [], [], [], [], []]

for i in range(len(semester)):
    semester[i].append(m for m in list)

print(semester)


list = [1, 2, 3, 4, 5, 6, [], [], []]
list.remove([])
print(list)
list.remove([])
print(list)
list.remove([])
print(list)


if 3 in list:
    return True
else:
    return False
