import queue


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if len(graph) <= 1:
            return False

        graph_ = {}
        set_A = []
        set_B = []

        for i in range(len(graph)):
            graph_[i] = graph[i]  # node => connects
        # print(graph_)

    # bfs

    def bfs(self, graph, set_A, set_B):
        que = queue.Queue()
        s = set()

        que.put(graph[0])

        while q.qsize():
            cur_node = que.get()
            if cur_node in s:
                continue
            s.add(cur_node)
            for n in graph[cur_node]:
                que.put(n)
