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
