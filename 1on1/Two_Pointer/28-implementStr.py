class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_str = len(haystack)
        if not needle:
            return 0
        elif len_needle > len_str:
            return -1

        i, j = 0, 0

        while i <= len_str - len_needle:
            if haystack[i] == needle[0]:
                tmp_i = i
                while j < len_needle:
                    if haystack[tmp_i] != needle[j]:
                        j = 0
                        break
                    else:
                        tmp_i += 1
                        j += 1
                if j == len_needle:
                    return i

            i += 1

        return -1
