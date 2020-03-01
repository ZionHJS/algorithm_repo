import collections


class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        n = len(S)
        m = len(words)
        if n < 3 or m < 1:
            return 0

        # code
        counter = collections.Counter(S)
        print("counter:", counter)
        for word in words:
            if len(word) < len(counter):
                words.remove(words)

        # helper
        def helper(word):  # i -> word, j -> S
            i, j = 0, 0
            while j < n:
                if counter[S[j]] >= 3:
                    if S[j+1] == S[j]:
                        j += 1

        count = 0
        for word in words:
            if helper(word):
                count += 1

        return count
