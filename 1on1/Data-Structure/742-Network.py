import queue


class Solution:
    def __init__(self):
        self.res_dis = []

    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        if len(times) < N-1:
            return -1

        node_graph = self.build_graph(times)
        print("node_graph:", node_graph)

        self.bfs(node_graph, K, N)
        print("res_dis:", self.res_dis)

        if len(self.res_dis) > 0:
            return min(self.res_dis)
        else:
            return -1

    def bfs(self, node_graph, K, N):
        q = queue.Queue()
        q.put([K, 0])
        s = set()
        s.add(K)

        while q.qsize():
            for i in range(q.qsize()):
                cur_node, cur_dis = q.get()
                if cur_node in node_graph:
                    for neighbor in node_graph[cur_node]:
                        if neighbor[0] not in s:
                            s.add(neighbor[0])
                            q.put([neighbor[0], cur_dis+neighbor[1]])
                        if len(s) == N:
                            self.res_dis.append(cur_dis+neighbor[1])

    def build_graph(self, times):
        node_graph = {}

        for edge in times:
            if edge[0] not in node_graph:
                node_graph[edge[0]] = []
            node_graph[edge[0]].append([edge[1], edge[2]])

        return node_graph
