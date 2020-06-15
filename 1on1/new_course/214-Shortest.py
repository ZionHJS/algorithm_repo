class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        ans = 0

        for i in range(len(s)//2+1)[::-1]:
            if s[:i] == s[i+1:2*i+1][::-1]:
                ans = i
                break
            elif s[:i+1] == s[s[i+1:2*i+1][::-1]]:
                ans = i+1
                break
        if ans >= len(s)//2-1:
            return s

        return s[2*ans+1:][::-1] + s


class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        tmp = s[0]
        mnc = ["-"]  # manacher
        for i in range(len(s)):
            mnc.append(s[i])
            mnc.append("#")
        mnc = mnc[:-1] + ["+"]
        exps = [0 for i in range(len(mnc))]
        ans = 0
        #print("mnc:", mnc)
        i, j, b = 1, 1, 0
        while j < len(mnc):
            while j < b:
                cur = mnc[j]

            if exps[i] == 0:
                l, r, tmp_b = i-1, i+1, 0
                while exps[l] == exps[r]:
                    tmp_b += 1
                exps[i] = tmp_b
                b = i+exps[i]

            if 2*exps[j]+1 > tmp and exps[j] == i:
                tmp = 2*exps[j]+1
                ans = i
            exps[j] = exps[j]
            j += 1

        return s[i:][::-1] + s
