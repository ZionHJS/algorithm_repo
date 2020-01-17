import queue


class Solution:
    def __init__(self):
        self.res = []

    def findOrder(self, num: int, pre: List[List[int]]) -> List[int]:
        if not num:
            return []

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
        print(indegree_map)

        # BFS
        q = queue.Queue()
        for i in range(num):
            if i not in indegree_map:
                # set.add(i)
                q.put(i)
        print(q)

        while q.qsize():
            cur = q.get()
            self.res.append(cur)
            for neighbor in graph[cur]:
                indegree_map[neighbor] -= 1
                if indegree_map[neighbor] == 0:
                    q.put(neighbor)

        # result
        if len(self.res) == num:
            return self.res
        else:
            return []
