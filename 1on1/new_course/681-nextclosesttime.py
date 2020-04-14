class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = []
        for i in range(len(time)):
            if time[i].isdigit():
                digits.append(time[i])
        digits.sort()
        ans = time
        min_dif = 1e9
        # validation

        def is_valid(idx, digit):
            if idx < 2:
                return 0 <= int(digit) < 24
            if 2 <= idx:
                digit = digit[2:]
                return 0 <= int(digit) < 60
            return True
        # compare_time

        def compare(time1):
            nonlocal time
            dif = (int(time1[:2])-int(time[:2]))*60 + \
                (int(time1[2:]) - int(time[3:]))
            return dif
        # nxt_time

        def nxt_time(cur_time, idx, digits):
            nonlocal min_dif, ans
            if len(cur_time) == len(digits):
                cur_dif = compare(cur_time)
                if cur_dif < min_dif and cur_dif > 0:
                    ans = cur_time
                    min_dif = cur_dif
                return
            for i in range(len(digits)):
                if is_valid(idx, cur_time+digits[i]):
                    nxt_time(cur_time+digits[i], idx+1, digits)
        nxt_time("", 0, digits)
        if ans == time:
            return "".join(digits[0]*2)+":"+"".join(digits[0]*2)
        ans = ans[:2]+":"+ans[2:]
        return ans
