# 第一遍 暴力解法 超时
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False

        memo = [False for _ in range(len(s)+1)]

        #memo[-1] = self.dfs(s, wordDict, memo)

        return self.dfs(s, wordDict, memo)

    def dfs(self, s, wordDict, memo):
        if s in wordDict:
            return True

        for i in range(len(s)-1, -1, -1):
            if s[i:] in wordDict:
                memo[i] = self.dfs(s[:i], wordDict, memo)
                if memo[i] == True:
                    return True
                else:
                    continue

        return False

# 第二遍 真正的memo

# 第三遍 dp
