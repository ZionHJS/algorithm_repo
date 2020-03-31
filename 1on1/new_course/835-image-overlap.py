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

        for i in range(1, 2*len(str_A)+1):
            temp_ans = 0
            if i <= len(str_A):
                compare_A, compare_B = str_A[-i:], str_B[:i]  # from 1 ~ n
                remainder = i % n
            else:
                # from n+1 ~ 2n
                compare_A, compare_B = str_A[:-
                                             (i-len(str_A))], str_B[i-len(str_A):]
                remainder = (2*len(str_A)-i) % n

            print("i:", i, "remainder:", remainder)
            print("com_A:", compare_A, "com_B:", compare_B)
            for j in range(len(compare_A)):
                if remainder == 0 or (j % 3 <= remainder and j % 3 > 0):
                    print("inhere!")
                    if compare_A[j] == compare_B[j] == "1":
                        temp_ans += 1
                        print("temp_ans+:", temp_ans)

            ans = max(ans, temp_ans)

        return ans
