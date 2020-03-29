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
