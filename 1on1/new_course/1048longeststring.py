import queue
import collections


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        dp = {}  # dp

        for w in sorted(words, key=len):
            #print("w:", w)
            tmp = [0]  # tmp => 记录上一层的[words]的最大深度
            for i in range(len(w)):
                if w[:i] + w[i+1:] in dp:
                    tmp.append(dp[w[:i] + w[i+1:]])
                dp[w] = max(tmp) + 1

        print("dp:", dp)

        return max(dp.values())
