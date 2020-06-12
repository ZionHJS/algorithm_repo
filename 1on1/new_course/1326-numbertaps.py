class Solution:
    def minTaps(self, n: int, R: List[int]) -> int:
        stack = [-1]  # index
        prevb = [-1]  # record index as boundary
        i = 0

        while i <= n:
            if i <= n and (R[i] == 0 or i-R[i] > prevb[-1]+1):
                i += 1
                continue
            while len(prevb) >= 2 and j-R[i] <= prevb[-2]:
                stack.pop()
                prevb.pop()
            stack.append(i)
            prevb.append(i+R[i])
            j = i+1
            #print("stack:", stack)
            while j <= n and j <= prevb[-1]:
                if R[j] != 0 and j+R[j] >= prevb[-1]:
                    while len(prevb) >= 2 and j-R[j] <= prevb[-2]:
                        stack.pop()
                        prevb.pop()
                    stack.append(j)
                    prevb.append(j+R[j])
                j += 1
            #print("prevb:", prevb)
            i = j
        #print("prevb:", prevb, "stack:", stack)
        while prevb[-1] > n:
            stack.pop()
            prevb.pop()
            if prevb[-1] < n:
                prevb.append(n)
                stack.append(n)
        #print("prevb:", prevb, "stack:", stack)
        #print("stack:", stack)
        if prevb[-1] >= n:
            return len(stack)-1
        else:
            return -1
