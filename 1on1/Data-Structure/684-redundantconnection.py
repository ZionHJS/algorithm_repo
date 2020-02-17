import queue


class Solution:
    def __init__(self):
        self.ans = []

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        if len(edges) < 3:
            return None

        graph = {}
        for edge in edges:
            if edge[0] not in graph:
                graph[edge[0]] = []
            graph[edge[0]].append(edge[1])
            if edge[1] not in graph:
                graph[edge[1]] = []
            graph[edge[1]].append(edge[0])
        print("graph:", graph)

        # bfs
        q = queue.Queue()
        visited = set()
        q.put(1)

        while q.qsize():
            cur_node = q.get()
            visited.add(cur_node)

            if cur_node in graph:
                for neighbor in graph[cur_node]:
                    if neighbor in visited:
                        if [cur_node, neighbor] in edges:
                            if [cur_node, neighbor] not in self.ans:
                                self.ans.append([cur_node, neighbor])
                        else:
                            if [neighbor, cur_node] not in self.ans:
                                self.ans.append([neighbor, cur_node])
                    else:
                        print("graph[neighbor]:", graph[neighbor])
                        graph[neighbor].remove(cur_node)
                        if len(graph[neighbor]) == 0:
                            del graph[neighbor]
                        else:
                            q.put(neighbor)

        print("self.ans:", self.ans)
        return self.ans
