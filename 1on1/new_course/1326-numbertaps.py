class Solution:
    def minTaps(self, n: int, R: List[int]) -> int:
        stack = [-1]  # index
        prevb = [-1]  # record index as boundary
        i = 0

        while i <= n:
            if i <= n and (R[i] == 0 or i-R[i] > prevb[-1]+1):
                i += 1
                continue
            stack.append(i)
            prevb.append(i+R[i])
            j = i+1
            #print("stack:", stack)
            while j <= n and j <= prevb[-1]:
                if (j-R[j] <= stack[-1]-R[stack[-1]]) or(stack[-1]-R[stack[-1]] <= 0 and j-R[j] <= 0):
                    # print("here?")
                    while stack[-1] >= 0 and ((j-R[j] <= stack[-1]-R[stack[-1]]) or (stack[-1]-R[stack[-1]] <= 0 and j-R[j] <= 0)):
                        # print("pop!")
                        stack.pop()
                        prevb.pop()
                    stack.append(j)
                    prevb.append(j+R[j])

                if j+R[j] > prevb[-1]:
                    while j-R[j] <= prevb[-2]+1:
                        stack.pop()
                        prevb.pop()
                    stack.append(j)
                    prevb.append(j+R[j])
                j += 1
            i = prevb[-1]+1
        #print("prevb:", prevb, "stack:", stack)
        while prevb[-1] > n:
            stack.pop()
            prevb.pop()
            if prevb[-1] < n:
                # print("nnnn")
                prevb.append(n)
                stack.append(n)
        #print("prevb:", prevb, "stack:", stack)
        if prevb[-1] >= n:
            return len(stack)-1
        else:
            return -1
