class Solution:
    def lengthOfLongestSubstringKDistinct(self, S: str, K: int) -> int:
        s = set()
        cnt = 0
        self.ans = 0

        def dfs(s, cnt, idx, S, K):
            if len(s) > K:
                self.ans = max(self.ans, cnt-1)
                return
            elif idx >= len(s)-1:
                self.ans = max(self.ans, cnt)
                return

            for i in range(idx+1, len(S)):
                if S[i] not in s:
                    dfs(s.add(S[i]), cnt+1, i, S, K)
                    s.discard(S[i])
                else:
                    dfs(s, cnt+1, i, S, K)
        return self.ans
