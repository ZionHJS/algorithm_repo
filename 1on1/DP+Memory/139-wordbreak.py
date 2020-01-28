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

# 第三遍 dp
