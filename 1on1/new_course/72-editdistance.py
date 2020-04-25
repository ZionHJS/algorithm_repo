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


class Solution:
    def minDistance(self, start: str, target: str) -> int:
        if not target:
            return len(start)
        elif not start:
            return len(target)

        chars = "abcdefghijklmnopqrstuvwxyz"
        if len(start) < len(target):  # make start always the longer one
            start, target = target, start

        # cnt_same
        def cnt_same(w1, w2):
            cnt = math.inf
            n = len(w1)
            for i in range(len(w1)):
                tmp_cnt = 0
                for pair in zip(w1[i:], w2):
                    if pair[0] == pair[1]:
                        tmp_cnt += 1
                cnt = min(cnt, i+(n-i-tmp_cnt)+i)
            return cnt

        # traverse
        ans = math.inf
        dif = len(start)-len(target)
        # dfs

        def dfs(longer):
            nonlocal ans, dif, target
            if len(longer) == len(target):
                cnt = cnt_same(longer, target)
                #print("longer:", longer, "target:", target, "cnt:", cnt)
                ans = min(ans, dif+cnt)
                return
            for i in range(len(longer)):
                new_longer = longer[:i]+longer[i+1:]
                dfs(new_longer)

        dfs(start)

        return ans
