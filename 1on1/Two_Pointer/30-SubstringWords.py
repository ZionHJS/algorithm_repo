import copy


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) > 0:
            single_len = len(words[0])
            words_total_len = single_len*len(words)
        s_len = len(s)
        if not words:
            return []
        elif not s or s_len < words_total_len:
            return []

        res = []
        i, j = 0, 0
        while i <= s_len - words_total_len:
            for item in words:
                if s[i] == item[0]:
                    tmp_i = i
                    tmp_words = copy.deepcopy(words)
                    while len(tmp_words) > 0:
                        j = tmp_i + single_len
                        tmp_s = s[tmp_i:j]
                        if tmp_s in tmp_words:
                            tmp_words.remove(tmp_s)
                        else:
                            break

                        if len(tmp_words) == 0:
                            res.append(j-words_total_len)
                        else:
                            tmp_i += single_len
                    break
            i += 1

        return res

# 尼玛这么牛逼的算法居然超时
