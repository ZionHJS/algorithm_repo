class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        self.boolean = False
        visited = set()

        def dfs(temp_s1, idx, cur_s3):
            visited.add((temp_s1, cur_s3))
            if len(temp_s1) == 0:
                if cur_s3 == s2:
                    self.boolean = True
                return

            for i in range(idx, len(cur_s3)):
                if self.boolean or len(cur_s3[i:]) < len(temp_s1):
                    break
                if temp_s1[0] == cur_s3[i]:
                    if (temp_s1[1:], cur_s3[:i]+cur_s3[i+1:]) not in visited:
                        dfs(temp_s1[1:], i, cur_s3[:i]+cur_s3[i+1:])

        dfs(s1, 0, s3)

        return self.boolean


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2 = len(s1), len(s2)
        if l1 + l2 != len(s3):
            return False

        last = set([(0, 0)])   # => (idx_1, idx_2) both start from 0

        for char in s3:
            current = set()
            for i, j in last:
                if i < l1 and s1[i] == char:
                    current.add((i + 1, j))
                if j < l2 and s2[j] == char:
                    current.add((i, j + 1))
            if not current:
                return False

            last = current

        return True


s = set()
s.add((1, 2))
s.add((3, 4))
s.add((5, 6))
s.add((6, 7))
print("cur_len:", len(s))

nxt_q = set()
print("tr or false:", not nxt_q)

left = right = 1
print("judge:", left == right == 1)
