import queue


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not num or not pre:
            return True

        # graph => course:[list of courses]
        graph = {}
        for i in range(num):  # labbeld from 0 to n-1
            graph[i] = []
        for i in range(len(pre)):
            graph[pre[i][1]].append(pre[i][0])  # post:[pres]

        # map records each course's indegree number
        indegree_map = {}
        for i in range(num):
            for pre in graph[i]:
                if pre not in indegree_map:
                    indegree_map[pre] = 1
                else:
                    indegree_map[pre] += 1

        # put course which's indegree = 0 into queue
        q = queue.Queue()
        for i in range(num):
            if i not in indegree_map:
                q.put(i)
        count = 0
        while q.qsize():
            cur = q.get()
            count += 1
            for pre in graph[cur]:
                indegree_map[pre] -= 1
                if indegree_map[pre] == 0:
                    q.put(pre)
        # return Boolean
        return count == num
