class Solution(object):
    def numDecodings(self, s):
        opt = [0]*len(s)
        opt[0] = 1
        if len(s) >=2:
            s_ = int(s[0:2])




s = '1234'
s_ = s[0:2]
print(s_)
print(int(s_))