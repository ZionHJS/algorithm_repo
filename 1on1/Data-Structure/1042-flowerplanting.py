import queue


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        flowers = [1, 2, 3, 4]
        res = [0 for _ in range(N)]

        path_dict = self.path_graph(paths)
        print("path_dict:", path_dict)
        garden_flower_map = {}
        for garden in path_dict:
            garden_flower_map[garden] = 0
        print("garden_flower_map:", garden_flower_map)

        # for-loop + bfs
        for flower in flowers:
            q = queue.Queue()
            s = set()
            q.put(1)
            s.add(1)
            garden_flower_map[1] = flower
            while q.qsize():
                for i in range(q.qsize()):
                    cur_garden = q.get()
                    for flower in flowers:
                        garden_flower_map[cur_garden] = flower
                        if is_plantable(flower, cur_garden, path_dict, garden_flower_map):
                            res[cur_garden-1] = flower
                            for neighbor in path_dict[cur_garden]:
                                q.put(neighbor)

    def is_plantable(self, flower, garden_num, path_dict, garden_flower_map):
        for neighbor in path_dict[garden_num]:
            if garden_flower_map[neighbor] == flower:
                return False
            else:
                return True

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
