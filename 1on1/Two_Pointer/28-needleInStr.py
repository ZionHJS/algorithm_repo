class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        len_str = len(haystack)
        if not needle or len_needle == len_str:
            return 0
        elif len_needle > len_str:
            return -1

        i, j = 0, 0

        while i <= len_str - len_needle:
            if haystack[i] == needle[0]:
                while j < len_needle:
                    if haystack[i] != needle[j]:
                        j = 0
                        break
                    else:
                        i += 1
                        j += 1
                if j == len_needle:
                    return i - len_needle

            i += 1

        return -1
