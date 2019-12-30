class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return 0
        elif not s:
            return -1

        single_len = len(words[0])
        words_total_len = single_len*len(words)
        s_len = len(s)

        words_start = []
        for item in words:
            words_start.append(item[0])

        res = []

        i, j = 0, 0
        while i <= s_len - words_total_len:
            if s[i] in words_start:
                tmp_words = words
                while i <= s_len - single_len:
                    j = i + single_len
                    tmp_s = s[i:j]
                    if tmp_s in tmp_words:
                        tmp_words.remove(tmp_s)
                    else:
                        break

                    if not tmp_words:
                        res.append(j-words_total_len)
                        break
                    else:
                        i += single_len
            i += 1

        return res
