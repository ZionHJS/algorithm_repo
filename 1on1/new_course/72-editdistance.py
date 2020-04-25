class Solution:
    def minDistance(self, start: str, target: str) -> int:
        if not target:
            return len(start)
        elif not start:
            return len(target)
        if len(start) < len(target):
            start, target = target, start  # make start always the longer one

        # put the short one to map with the longer one
        def cnt_same(start, tmp_t):
            cnt, i, j = 0, 0, 0
            while i < len(start) and j < len(tmp_t):
                while start[i] != tmp_t[j]:
                    i += 1
                    if i >= len(start):
                        return 0
                j += 1
                i += 1
                cnt += 1
            return cnt

        # traverse
        ans = math.inf
        for j in range(len(target)):
            tmp_cnt = cnt_same(start, target[j:])
            tmp_ans = (len(start)-len(target)) + (len(target) - tmp_cnt)
            ans = min(ans, tmp_ans)

        return ans
