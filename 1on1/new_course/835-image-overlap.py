class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        ans = 0
        str_A, str_B = "", ""

        for i in range(n):
            for j in range(n):
                str_A += str(A[i][j])
                str_B += str(B[i][j])
        print("str_A:", str_A, "str_B:", str_B)

        for i in range(n):
            for j in range(n):
                tmp_ans_A, tmp_ans_B = 0, 0
                for k in range((i+1)*n):
                    #print("k:", k)
                    if k % n <= j:
                        #print("k%n:", k%n, "j:", j)
                        if str_A[-k-1] == str_B[k] == 1:
                            print("inhere!")
                            tmp_ans_A += 1
                        if str_B[-k-1] == str_A[k] == 1:
                            tmp_ans_B += 1
                print("tmp_ans_A:", tmp_ans_A, "tmp_ans_B:", tmp_ans_B)
                ans = max(ans, tmp_ans_A, tmp_ans_B)

        return ans
