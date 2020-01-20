class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']

        res = []
        left, right = self.get_leftright_count(s)
        self.dfs(res, left, right, 0, s)
        return res

    def dfs(self, res, left, right, index, s):
        if left == 0 and right == 0:
            if self.isvalid(s):
                res.append(s)
                return

        for i in range(index, len(s)):
            if i > index and s[i] == s[i-1]:
                continue

            if s[i] == '(':
                self.dfs(res, left-1, right, i, s[:i] + s[i+1:])
            if s[i] == ')':
                self.dfs(res, left, right-1, i, s[:i] + s[i+1:])

    def isvalid(self, s):
        left, right = self.get_leftright_count(s)
        return left == 0 and right == 0

    def get_leftright_count(self, s):
        left = right = 0
        for c in s:
            if c == '(':
                left += 1
            if c == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        return left, right
