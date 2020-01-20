import queue


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:
            return 0

        graph = {}
        circle_count = 0

        # build the graph
        for i in range(len(M)):
            graph[i] = []
            for j in range(len(M)):
                if M[i][j] == 1 and i != j:
                    graph[i].append(j)
        # print(graph)

    def bfs(self, graph, stu, count):
        q = queue.Queue()
        s = set()
        q.put(stu)

        while q.qsize():
            cur_stu = q.get()
            s.add(cur_stu)
            if graph[cur_stu]:
                for friend in graph[cur_stu]:
                    if friend not in s:
                        q.put(friend)

        return count += 1
