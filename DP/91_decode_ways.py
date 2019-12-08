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




class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        if(not s or s[0]=="0"): #头位非零判断
            return 0

        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(1,n):
            if(s[i]=="0"):
                if(s[i-1]=="1" or s[i-1]=="2"):
                    dp[i+1]=dp[i-1]
                else:
                    return 0
            else:
                if(s[i-1]=="1" or (s[i-1]=="2" and "1"<=s[i]<="6")):
                    dp[i+1]=dp[i]+dp[i-1]
                else:
                    dp[i+1]=dp[i]
        return dp[-1]




class Solution:
    def numDecodings(self, s)
        pp, p = 1, int(s[0] != '0')
        for i in range(1, len(s)):
            pp, p = p, pp * (9 < int(s[i-1:i+1]) <= 26) + p * (int(s[i]) > 0)
        return p
