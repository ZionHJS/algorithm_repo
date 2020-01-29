#memo:  (超时)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not dict:
            return False

        memo = [False for _ in range(len(s) + 1)]
        memo[0] = True

        self.dfs(len(s), s, wordDict, memo)

        return memo[-1]

    def dfs(self, index, s, wordDict, memo):
        if index == 0 or memo[index] != False:
            return memo[index]

        for word in wordDict:
            if word == s[len(s)-len(word):index]:
                memo[index] = self.dfs(
                    index-len(word), s[:len(s)-len(word)], wordDict, memo)
                if memo[index] == True:
                    return True

        return False

# 第二遍 真正的memo


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}
        return self.dfs(s, memo, wordDict)

    def dfs(self, s, memo, wordDict):
        if s in memo:
            return memo[s]  # 返回键memo[s]对应的值
        if s in wordDict:
            memo[s] = True
            return True

        for i in range(1, len(s)):
            left = s[0:i]
            right = s[i:]
            if right in wordDict and self.dfs(left, memo, wordDict):
                memo[s] = True
                return True

            memo[s] = False

        return False

# 第三遍 dp
