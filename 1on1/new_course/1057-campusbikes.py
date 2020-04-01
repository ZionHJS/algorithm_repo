import heapq


class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        n, m = len(workers), len(bikes)
        visited_w, visited_b, heaps, ans = set(), set(), [], [-1 for i in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                res_i = self.get_dis(workers[i], bikes[j])
                heapq.heappush(heaps, (res_i, (i, j)))

        while len(heaps) > 0:
            cur_ans = heapq.heappop(heaps)
            if (cur_ans[1][0] not in visited_w) and (cur_ans[1][1] not in visited_b):
                ans[cur_ans[1][0]] = cur_ans[1][1]
                visited_w.add(cur_ans[1][0]), visited_b.add(cur_ans[1][1])

        return ans

    def get_dis(self, worker, bike):
        dis = abs(worker[0]-bike[0])+abs(worker[1]-bike[1])
        return dis
