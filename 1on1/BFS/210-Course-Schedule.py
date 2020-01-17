import queue


class Solution:
    def __init__(self):
        self.res = []

    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        if num <= 1 or not pre:
            return numCourses

        # graph
        graph = {}
        for i in range(num):
            graph[i] = []
            for n in pre:
                graph[n[1]].append(n[0])  # key:val => pre:[post]
        print(graph)

        # indegree count{}
        indegree_map = {}
        for i in range(num):
            for neighbor in graph[i]:
                if neighbor not in indegree_map:
                    indegree_map[neighbor] = 1
                else:
                    indegree_map[neighbor] += 1

        # BFS
        q = queue.Queue()
        s = set()
        for i in range(num):
            if i not in indegree_map:
                set.add(i)
                self.res.append(i)
                q.put(i)

        while q.qsize():
            cur = q.get()
            if cur in s:
                continue
            self.res.append(cur)
            for neighbor in graph[cur]:
                indegree_map[neighbor] -= 1
                if indegree_map[neighbor] == 0:
                    q.put(neighbor)

        # result
        if len(self.res) == num:
            return self.res
        else:
            return False
