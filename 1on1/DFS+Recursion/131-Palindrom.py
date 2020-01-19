class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []

        res = []
        temp = []
        self.dfs(res, temp, s)
        return res

    def dfs(self, res, temp, s):
        if len(s) == 0:
            res.append(temp[:])
            return

        for i in range(1, len(s) + 1):
            prefix = s[:i]
            if self.is_palindrome(prefix):
                temp.append(prefix)
                self.dfs(res, temp, s[i:])
                temp.pop()

    def is_palindrome(self, prefix):
        return prefix == prefix[::-1]  # => [::-1] => reverse order
