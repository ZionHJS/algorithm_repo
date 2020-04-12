import collections


class Solution:
    def findWords(self, B: List[List[str]], words: List[str]) -> List[str]:
        graph = collections.defaultdict(lambda: [])
        for word in words:
            graph[word[0]].append(word)
        m, n = len(B[0]), len(B)
        ans, memo = set(), collections.defaultdict(lambda: False)
        x_, y_ = [-1, 1, 0, 0], [0, 0, -1, 1]
        #print("graph:", graph)
        for i in range(n):
            for j in range(m):
                if B[i][j] in graph:
                    for target in graph[B[i][j]]:
                        if target not in ans:
                            visited = set()
                            if self.dfs(m, n, i, j, target, 0, B, x_, y_, visited, memo):
                                ans.add(target)
        return ans

    def dfs(self, m, n, y, x, target, idx, B, x_, y_, visited, memo):
        if idx == len(target)-1:
            return True
        elif memo[(y, x, idx, target)]:
            return True
        elif B[y][x] != target[idx]:
            return False
        visited.add((y, x))
        for i in range(4):
            nxt_x, nxt_y = x+x_[i], y+y_[i]
            if self.is_valid(nxt_y, nxt_x, m, n) and (nxt_y, nxt_x) not in visited and B[nxt_y][nxt_x] == target[idx+1]:
                if self.dfs(m, n, nxt_y, nxt_x, target, idx+1, B, x_, y_, visited, memo):
                    memo[(y, x, idx, target)] = True
                    return True
        visited.discard((y, x))
        return False

    def is_valid(self, y, x, m, n):
        return 0 <= x < m and 0 <= y < n
