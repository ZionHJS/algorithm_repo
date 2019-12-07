class Solution(object):
    def numDecodings(self, s):
        s_len = len(s)
        opt = [1]*s_len
        if int(s[0]) == 0:
            return 0

        if len(s) >=2:
            s_ = s[0:2]
            if int(s_) <= 26 and int(s_[1:2]) !=0:
                opt[1] = 2
            elif int(s_) <= 26 and int(s_[1:2]) == 0:
                opt[1] = 1

        for i in range(2, s_len):
            if int(s[i]) == 0 and int(s[i-1]) == 0:
                opt[i] = 0
            elif int(s[i]) == 0 and int(s[i-1:i+1]) > 26:
                opt[i] = 0
            elif int(s[i]) == 0 and int(s[i-1:i+1]) <= 26:
                opt[i] = opt[i-2]
            elif int(s[i-1]) == 0 and int(s[i-2:i]) > 26:
                opt[i] = 0
            elif int(s[i-1]) == 0 and int(s[i-2:i]) <= 26:
                opt[i] = opt[i-1]
            elif int(s[i-1:i+1]) > 26:
                opt[i] = opt[i-1]
            elif int(s[i-1:i+1]) <= 26:
                opt[i] = opt[i-1] + opt[i-2]
        return opt[-1]

s = '1234'
s_ = s[0:2]
print(s[0])
print(s_)
print(int(s_))

s = '1234'
opt = [0]
print(opt[-1])
print(s[0])

