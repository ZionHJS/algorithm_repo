class Solution:
    def minWindow(self, S: str, T: str) -> str:
        if len(S) < len(T):
            return ""
        if len(T) == 1:
            if T in S:
                return T
            else:
                return ""

        self.res = [S+"123"]
        #print("self.res:", self.res)
        for i in range(len(S)):
            if i >= 1 and S[i] == S[i-1]:
                continue
            if S[i] == T[0]:
                if len(S[i:]) >= len(T):
                    self.getW(S[i:], T)
                    if len(self.res[0]) == len(T):
                        return T
            #print("self.res:", self.res)
        if self.res[0] != S+"123":
            return self.res[0]
        else:
            return ""

    def getW(self, cur_s, T):
        i, j = 1, 1
        while j < len(T) and i < len(cur_s):
            while i < len(cur_s) and cur_s[i] != T[j]:
                i += 1
            if i < len(cur_s):
                i += 1
            j += 1
        # if j == len(T) and cur_s[i-1] == T[j-1]:
        if j == len(T):
            if cur_s[i-1] == T[j-1]:
                if len(cur_s[:i]) < len(self.res[-1]):
                    self.res = [cur_s[:i]]
                elif len(cur_s[:i]) == len(self.res[-1]):
                    self.res.append(cur_s[:i])


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T):
                return i
            if (i, j) not in memo:
                ind = S.find(T[j], i + 1)
                if ind != -1:
                    memo[(i, j)] = dfs(ind, j+1)
                else:
                    memo[(i, j)] = float('inf')
                #memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]

        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                # 从T[1]开始 在 S[i+1:] 中找 每个 char  看是否能找到所有的char 如果不能找到所有 就返回 inf
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]
        return res


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T):
                return i
            if (i, j) not in memo:
                tmp_idx = S.find(T[j], i + 1)
                if tmp_idx != -1:
                    memo[(i, j)] = dfs(tmp_idx, j+1)
                else:
                    memo[(i, j)] = float('inf')
                #memo[(i, j)] = float('inf') if ind == -1 else dfs(ind, j + 1)
            return memo[(i, j)]

        l, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                # 从T[1]开始 在 S[i+1:] 中找 每个 char  看是否能找到所有的char 如果不能找到所有 就返回 inf
                j = dfs(i, 1)
                if j - i < l:
                    l, res = j - i, S[i:j + 1]
        return res


class Solution:
    def minWindow(self, S: str, T: str) -> str:
        def dfs(i, j):
            if j == len(T):  # exit! if success and find the end
                return i
            if (i, j) not in memo:
                tmp_idx = S.find(T[j], i + 1)
                if tmp_idx != -1:
                    memo[(i, j)] = dfs(tmp_idx, j+1)
                else:
                    memo[(i, j)] = float('inf')  # exit! not find to the end
            return memo[(i, j)]

        tmp_len, res, memo = float('inf'), '', {}
        for i, s in enumerate(S):
            if s == T[0]:
                # 从T[1]开始 在 S[i+1:] 中找 每个 char  看是否能找到所有的char 如果不能找到所有 就返回 inf
                tmp_end_idx = dfs(i, 1)
                if tmp_end_idx+1-i < tmp_len:
                    tmp_len, res = tmp_end_idx+1-i, S[i:tmp_end_idx + 1]
        return res
