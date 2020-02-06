class Solution:
    """
    @param s: a string
    @param k: an integer
    @return: the number of substrings there are that contain at least k distinct characters
    """

    def kDistinctCharacters(self, s, k):
        if not s or k == 0:
            return 0
        elif k == 1:
            return len(s)

        alpha_counts = [0 for _ in range(256)]
        count = 0
        res = 0
        i, j = 0, 0

        while j < len(s):
            char = ord(s[j])
            alpha_counts[char] += 1
            if alpha_counts[char] == 1:
                count += 1

            if count == k:
                res += 1
                tmp_alpha_counts = alpha_counts
                tmp_i = i
                tmp_count = count

                while tmp_i < j and tmp_count == k:
                    tmp_char = ord(s[tmp_i])
                    tmp_alpha_counts[tmp_char] -= 1
                    if tmp_alpha_counts[tmp_char] == 0:
                        tmp_count -= 1
                    if tmp_count == k:
                        res += 1
                    tmp_i += 1
                j += 1
                continue

            while i < j and count >= k):
                char=ord(s[i])
                alpha_counts[char] -= 1
                if alpha_counts[char] == 0:
                    counts -= 1
                if count == k:
                    res += 1
                i += 1

            j += 1

        return res
