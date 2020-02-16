import queue


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [1, 2, 3, 4]
        res = [0 for _ in range(N)]

        path_dict = self.path_graph(paths)
        garden_flower_map = {}
        for garden in path_dict:
            garden_flower_map[garden] = 0

        #bfs + dfs

    def bfs(self, garden, garden_flower_map, flowers):
        q = queue
        s = set()
        q.put(garden)
        s.add(garden)

        while q.qsize():
            cur_garden = q.get()

    def path_graph(self, paths):
        path_dict = {}
        for path in paths:
            if (path[0] not in path_dict):
                path_dict[path[0]] = []
            if (path[1] not in path_dict):
                path_dict[path[1]] = []

            path_dict[path[0]].append(path[1])
            path_dict[path[1]].append(path[0])

        return path_dict
