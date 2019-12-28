class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        alph_counts = [0 for _ in range(256)]
        count = 0
        max_len = 0
        i, j = 0, 0

        while j < len(s):
            char = ord(s[j])
            alph_counts[char] += 1
            if alph_counts[char] > 1:
                count += 1
            while i < len(s) and count >= 1:
                char = ord(s[i])
                alph_counts[char] -= 1
                if alph_counts[char] == 1:
                    count -= 1
                i += 1
            max_len = max(max_len, j-i+1)
            j += 1

        return max_len
