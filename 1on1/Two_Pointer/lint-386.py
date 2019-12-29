class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """

    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s or k == 0:
            return 0

        alpha_counts = [0 for _ in range(256)]
        count = 0
        max_len = 0
        i, j = 0, 0

        while j < len(s):
            char = ord(s[j])
            alpha_counts[char] += 1
            if alpha_counts[char] == 1:
                count += 1

            while i < j and count > k:
                char = ord(s[i])
                alpha_counts[char] -= 1
                if alpha_counts[char] == 0:
                    count -= 1
                i += 1

            max_len = max(max_len, j-i+1)

            j += 1

        return max_len
