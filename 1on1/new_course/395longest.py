import collections


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if not s:
            return 0
        ans = 0
        counter = {}

        def dfs(idx, sub, counter):
            nonlocal s, k, ans
            if idx == len(s):
                return
            counter[s[idx]] = counter[s[idx]]+1 if s[idx] in counter else 1
            if min(counter.values()) >= k:
                ans = max(ans, len(sub))
            if (len(s)-1-idx)+len(sub) > ans:
                dfs(idx+1, sub+s[idx], counter)
            counter[s[idx]] -= 1
            if counter[s[idx]] == 0:
                del counter[s[idx]]

        for i in range(len(s)):
            if i > 1 and s[i] == s[i-1]:
                continue
            dfs(i, str(s[i]), counter)

        return ans
