import queue


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        if len(graph) == 1:
            return len(graph[0])

        graph_ = {}
        count = 0

        for i in range(len(graph)):
            graph_[i] = graph[i]

        self.dfs(graph_)

    def dfs(self, graph):
        #q = queue.Queue()
        #s = set()
        for key in graph:
