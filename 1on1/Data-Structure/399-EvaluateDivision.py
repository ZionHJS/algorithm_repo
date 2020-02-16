class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        if not equations:
            return -1

        eve_graph = self.build_eve_graph(equations, values)

        res = []
        for query in queries:
            res.append(self.getEvaluate(eve_graph, query[0], query[1], 1))

    def getEvaluate(self, eve_graph, in_char, out_char, cur_eve):
        for neighbor in eve_graph[in_char]:
            if neighbor[1] == out_char:
                return cur_eve*neighbor[0]

            new_eve = cur_eve*neighbor[0]
            ans = self.getEveluate(eve_graph, neighbor, out_char, new_eve)
            if ans:
                return ans

        return -1

    def build_eve_graph(self, equations, values):
        eve_graph = {}

        for i in range(len(equations)):
            if equations[i][0] not in eve_graph:
                eve_graph[equations[i][0]] = []

            eve_graph[equations[i][0]].append([values[i], equations[i][1]])

        return eve_graph


a = [(2, 3), (4, 5)]
a.append((7, 8))
a = [(2, 3)]
for neighbor in a:
    print("now)neighbor:", neighbor)
print("a:", a)
print("a[0]:", a[0])
print("a[1][1]:", a[1][1])
