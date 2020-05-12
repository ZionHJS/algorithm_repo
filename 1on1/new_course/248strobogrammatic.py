class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        dic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        dic_list = ["0", "1", "6", "8", "9"]

        # cnt_all valid length
        m, n, cnt_all = len(low), len(high), 0
        for i in range(m, n+1):
            if 0 < i <= 2:
                cnt_all += 4
            else:
                cnt_all += 4*(5**((i-2)//2 if not i % 2 else (i-3)//2+1))

        # shave bottom and top
        # for bottom
        cnt_bt = 1
        low = []
        for i in range(m//2 if m % 2 else m//2+1):
            tmp = []
            for key in dic:
                if int(key) <= int(low[i]):
                    tmp.append(key)
            low.append(tmp)

        # for top
        cnt_tp = 1
        top = []
        for i in range(n):
            tmp = []
            for key in dic:
                if int(key) >= int(low[i]):
                    tmp.append(key)
            top.append(tmp)
        cnt_tp *= len(x) if len(x) for x in high if high

        return cnt_all-cnt_bt-cnt_tp
