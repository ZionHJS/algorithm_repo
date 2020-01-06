import queue


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if len(edges) != n-1:
            return False

        # initialize graph
        graph = self.initialize_graph(n, edges)

        # BFS
        q = queue.Queue()
        s = set()
        q.put(0)
        s.add(0)
        while q.qsize():
            node = q.get()
            for neighbor in graph[node]:
                if neighbor not in s:
                    s.add(neighbor)
                    q.put(neighbor)

        # boolean
        return len(s) == n

    def initialize_graph(self, n, edges):
        graph = {}
        for i in range(n):
            graph[i] = set()

        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[v].add(u)
            graph[u].add(v)

        return graph
