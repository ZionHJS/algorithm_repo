class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        n = len(username)
        web_s = set(website)
        graph = {}
        for i in range(n):
            if username[i] not in graph:
                graph[username[i]] = []
            graph[username[i]].append(website[i])
        # 1.get combination dfs()
        self.combination, temp = [], []
        self.dfs(0, website, temp)
        #print("combination:", self.combination)
        # 2.count for each combination
        self.res = [[], 0]
        for combination in self.combination:
            self.sites_in_user(combination, graph)
        return self.res[0]

    def dfs(self, idx, website, temp):
        if len(temp) == 3:
            if temp not in self.combination:
                self.combination.append(temp[:])
            return
        elif idx >= len(website):
            return
        for i in range(idx, len(website)):
            temp.append(website[i])
            self.dfs(idx+1, website, temp)
            temp.pop()

    def sites_in_user(self, combination, graph):
        count = 0
        for key in graph:
            i, j = 0, 0
            while i < len(combination) and j < len(graph[key]):
                if combination[i] == graph[key][j]:
                    i += 1
                    j += 1
                else:
                    j += 1
            if i == len(combination):
                count += 1
        if count > self.res[1]:
            self.res = [combination, count]
