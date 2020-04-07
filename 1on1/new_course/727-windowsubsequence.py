class Solution:
    def minWindow(self, S: str, T: str) -> str:
        if len(S) < len(T):
            return ""
        if len(T) == 1:
            if T in S:
                return T
            else:
                return ""

        self.res = [S+"123"]
        #print("self.res:", self.res)
        for i in range(len(S)):
            if i >= 1 and S[i] == S[i-1]:
                continue
            if S[i] == T[0]:
                if len(S[i:]) >= len(T):
                    self.getW(S[i:], T)
                    if len(self.res[0]) == len(T):
                        return T
            #print("self.res:", self.res)
        if self.res[0] != S+"123":
            return self.res[0]
        else:
            return ""

    def getW(self, cur_s, T):
        i, j = 1, 1
        while j < len(T) and i < len(cur_s):
            while i < len(cur_s) and cur_s[i] != T[j]:
                i += 1
            if i < len(cur_s):
                i += 1
            j += 1
        # if j == len(T) and cur_s[i-1] == T[j-1]:
        if j == len(T):
            if cur_s[i-1] == T[j-1]:
                if len(cur_s[:i]) < len(self.res[-1]):
                    self.res = [cur_s[:i]]
                elif len(cur_s[:i]) == len(self.res[-1]):
                    self.res.append(cur_s[:i])
