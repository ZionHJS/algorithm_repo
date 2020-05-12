class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        if int(low) > int(high):
            return 0
        dic = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        list_all = set(["0", "1", "6", "8", "9"])
        list_mid = set(["0", "1", "8"])
        # cnt_all valid length
        m, n, cnt_all = len(low), len(high), 0
        for i in range(m, n+1):
            if i == 1:
                cnt_all += 5
            elif i == 2:
                cnt_all += 4
            else:
                cnt_all += 4*(5**((i-2)//2))*(3 if i % 2 else 1)

        # dfs() to shave bottom and top
        remove = set()

        def build(idx, rg, cur, target, bt):
            if idx > rg:
                if not len(target) % 2:
                    for c in cur[::-1]:
                        cur += dic[c]
                else:
                    for c in cur[:-1][::-1]:
                        cur += dic[c]
                if bt:  # if low
                    if int(cur) < int(target):
                        remove.add(cur)
                else:  # if high
                    if int(cur) > int(target):
                        remove.add(cur)
                return

            if not len(target) % 2:
                for c in list_all:
                    build(idx+1, rg, cur+c, target, bt)
            else:
                if idx <= rg-1:
                    for c in list_all:
                        build(idx+1, rg, cur+c, target, bt)
                else:
                    for c in list_mid:
                        build(idx+1, rg, cur+c, target, bt)
        rglow = m//2 if not m % 2 else m//2+1
        rghigh = n//2 if not n % 2 else n//2+1
        if len(low) > 1:
            for start in list_all:
                if 0 < int(start) <= int(low[0]):
                    build(2, rglow, start, low, True)
        else:
            for start in list_all:
                if (start not in list_mid) or (int(start) < int(low[0])):
                    remove.add(start)
        if len(high) > 1:
            for start in list_all:
                if int(start) >= int(high[0]):
                    build(2, rghigh, start, high, False)
        else:
            for start in list_all:
                if (start not in list_mid) or (int(start) > int(high[0])):
                    remove.add(start)

        return cnt_all-len(remove)
