import queue


class Solution:
    def findOrder(self, nums: int, pres: List[List[int]]) -> List[int]:
        if not nums:
            return []
        elif not pres:
            res = []
            for i in range(nums):
                res.append(i)
            return res

        # create a prerequisite graph map
        graph = {}
        for i in range(nums):
            graph[i] = set()
        for edge in pres:
            graph[edge[1]].add(edge[0])  # pre:post

        # indegree map
        indegree = {}
        for course in graph:
            for post_course in graph[course]:
                if post_course not in indegree:
                    indegree[post_course] = 1
                else:
                    indegree[post_course] += 1

        # bfs queue
        q = queue.Queue()
        res = []
        for course in graph:
            if course not in indegree:
                q.put(course)

        print(q.qsize())
        print(graph)
        print(indegree)

        while q.qsize():
            cur = q.get()
            print(cur)
            res.append(cur)
            for post_course in graph[cur]:
                indegree[post_course] -= 1
                if indegree[post_course] == 0:
                    q.put(post_course)

        if len(res) == nums:
            return res
        else:
            return []
