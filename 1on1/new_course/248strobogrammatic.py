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
                cnt_all += 4*(5**((i-2)//2))*(3 if i % 2 else 1)
        print("cnt_all:", cnt_all)

        # shave bottom and top
        # for bottom
        cnt_bt = 1
        bt = []
        cur_b = 1
        rg_b = (m//2) if not m % 2 else (m//2)+1
        for i in range(rg_b):
            #print("i:", i)
            tmp = []
            for key in dic:
                if int(key) <= int(low[i]):
                    print("low[i]:", low[i])
                    tmp.append(key)
            print("tmp:", tmp)
            if i == 0:
                if tmp[-1] != low[i] or low[i] not in dic:
                    cur_b *= 0
            else:
                cur_b *= len(tmp)
            bt.append(tmp)
        print("cur_b:", cur_b)
        cnt_bt += cur_b
        if 0 < m <= 2:
            cnt_bt += len(bt[0])-1 if len(bt[0]) >= 1 else len(bt[0])
        else:
            cnt_bt += (len(bt[0])-1)*((5**(m-2)//2))*(3 if m %
                                                      2 else 1) if len(bt[0]) >= 1 else len(bt[0])

        # for top
        cnt_tp = 1
        tp = []
        cur_t = 1
        rg_t = (n//2) if not n % 2 else (n//2)+1
        for i in range(rg_t):
            tmp = []
            for key in dic:
                if int(key) >= int(high[i]):
                    tmp.append(key)
            if i == 0:
                if tmp[0] != high[i] or high[i] not in dic:
                    cur_t *= 0
            else:
                cur_t *= len(tmp)
            tp.append(tmp)
        print("cur_t:", cur_t)
        cnt_tp += cur_t
        if 0 < n <= 2:
            cnt_tp += len(bt[0])-1 if len(bt[0]) >= 1 else len(bt[0])
        else:
            cnt_tp += (len(tp[0])-1)*((5**(n-2)//2))*(3 if n %
                                                      2 else 1) if len(tp[0]) >= 1 else len(tp[0])

        return cnt_all-cnt_bt-cnt_tp
