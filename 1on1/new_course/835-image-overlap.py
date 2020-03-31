def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
    self.n, self.ans, str_A, str_B = len(A), 0, "", ""
           # make List_A and List_B to a continuously string first , then we compare from 1d-emensional rather than 2d-mensional
    for i in range(self.n):
        for j in range(self.n):
            str_A += str(A[i][j])
            str_B += str(B[i][j])

    # our compare def to compare two string when they are overlaped
    def compare(str_1, str_2):
        for i in range(1, len(str_A)+1):
            temp_ans = 0
            compare_1, compare_2 = str_1[-i:], str_2[:i]  # from 1 ~ n
            remainder = i % self.n

               # count
               for j in range(len(compare_1)):
                    if remainder == 0 or ((j+1) % self.n <= remainder and (j+1) % self.n > 0):
                        if compare_1[j] == compare_2[j] == "1":
                            temp_ans += 1
                self.ans = max(self.ans, temp_ans)  # get the max count

    compare(str_A, str_B)
    compare(str_B, str_A)

    return self.ans
