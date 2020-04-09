class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p) or not s or not p:
            return []
        cnt_p = collections.Counter(p)
        cnt_s = collections.Counter(s[:len(p)])
        res = []
        for i in range(len(s)-len(p)+1):
            if i != 0:
                j = i + len(p) - 1
                cnt_s[s[j]] += 1
            is_ana = cnt_p == cnt_s
            if is_ana:
                res.append(i)
            cnt_s[s[i]] -= 1
            if cnt_s[s[i]] == 0:
                del cnt_s[s[i]]
        return res
