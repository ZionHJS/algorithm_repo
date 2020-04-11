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


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=lambda x: len(x))   # O(N*logN)
        min_len, n, max_len, visited, done = len(words[0]), len(
            words), 0, collections.defaultdict(lambda: 0), {}

        # bfs
        q = queue.Queue()
        for i in range(n):
            q.put(words[i])
        while q.qsize():
            max_len += 1
            m = q.qsize()
            #print("m:", m)
            for i in range(m):
                cur_word = q.get()
                for i in range(n):
                    if len(cur_word)+1 > len(words[i]):
                        continue
                    elif len(cur_word)+1 == len(words[i]):
                        if self.is_nxt(cur_word, words[i]):
                            q.put(words[i])
                            visited[words[i]] += 1
                    elif len(cur_word)+1 < len(words[i]):
                        break

        return max_len

    def is_nxt(self, word1, word2):
        for i in range(len(word2)):
            left, right = word2[:i], word2[i+1:]
            word2_ = left+right
            if word1 == word2_:
                return True
        return False
