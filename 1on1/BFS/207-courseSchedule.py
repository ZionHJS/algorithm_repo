import queue


class Solution:
    def canFinish(self, num: int, pre: List[List[int]]) -> bool:
        if not num or not pre:
            return True

        # graph => course:[list of courses]
        graph = {}
        for i in range(num):  # labbeld from 0 to n-1
            graph[i] = []
        for i in range(len(pre)):
            graph[pre[i][1]].append(pre[i][0])  # pre:[post]

        # map records each course's indegree number
        indegree_map = {}
        for i in range(num):
            for post in graph[i]:  # ??? at least it is a [], you can for in []
                if post not in indegree_map:
                    indegree_map[post] = 1
                else:
                    indegree_map[post] += 1

        # put course which's indegree = 0 into queue
        q = queue.Queue()
        for i in range(num):
            if i not in indegree_map:  # put the node into the queue starts with these without pres
                q.put(i)
        count = 0
        while q.qsize():
            cur = q.get()
            count += 1
            for post in graph[cur]:
                indegree_map[post] -= 1
                if indegree_map[post] == 0:
                    q.put(post)
        # return Boolean
        return count == num  # did we counted all the courses???
