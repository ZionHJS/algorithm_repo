class Solution:
    def minimumDistance(self, word: str) -> int:
        # build the board   0~26   x=6, y=5
        chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        B = collections.defaultdict(lambda: [])
        for k in range(26):
            (d, r) = divmod(k, 6)
            B[chars[k]] = [d, r]
        res = math.inf

        # divide the board
        def dfs(cur_dis, prev_l, prev_r, idx, word):
            nonlocal res
            if idx >= len(word):
                res = min(res, cur_dis)
                return
            elif cur_dis >= res:  # optimize
                return
            # try left-finger
            if prev_l:
                tmp_dis = abs(B[word[idx]][0]-B[prev_l][0]) + \
                    abs(B[word[idx]][1]-B[prev_l][1])
                if tmp_dis < 5:  # optimize
                    dfs(cur_dis+tmp_dis, word[idx], prev_r, idx+1, word)
            else:
                dfs(cur_dis, word[idx], prev_r, idx+1, word)
            # try right-finger
            if prev_r:
                tmp_dis = abs(B[word[idx]][0]-B[prev_r][0]) + \
                    abs(B[word[idx]][1]-B[prev_r][1])
                if tmp_dis < 5:  # optimize
                    dfs(cur_dis+tmp_dis, prev_l, word[idx], idx+1, word)
            else:
                dfs(cur_dis, prev_l, word[idx], idx+1, word)

        dfs(0, "", "", 0, word)

        return res
