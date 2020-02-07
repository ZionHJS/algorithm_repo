class Solution:
    def maxEnvelopes(self, List: List[List[int]]) -> int:
        if not List:
            return 0

        n = len(List)

        # w s => l
        for i in range(2, n):
            for j in range(i, 0, -1):
                if List[j][0] < List[j-1][0]:
                    List[j][0], List[j-1][0] = List[j-1][0], List[j][0]
        # h s => l
        for i in range(2, n):
            for j in range(i, 0, -1):
                if List[j][0] == List[j-1][0]:
                    if List[j][1] < List[j-1][1]:
                        List[j][1], List[j-1][1] = List[i-1][1], List[i][1]

        #print("list:", List)
        for i in range(n):
            print(List[i])

        #left, right = 0, n-1
        idx = n-1
        count_env = 1
        prev_env = List[idx]

        while idx >= 0:
            left, right = 0, idx
            lp_idx = self.lp_bs(left, right)
            fp_idx = self.fp_bs(left, lp_idx)

            if self.next_envelope(fp_idx, lp_idx, prev_env) != None:
                count_env += 1
                prev_env = self.next_envelope(fp_idx, lp_idx, prev_env)
            idx = fp_idx

        return count_env

    def lp_bs(self, left, right):  # => right
        while left + 1 < right:
            mid = left + (right-left)//2
            if List[mid][0] == List[right][0]:
                right = mid
            else:
                left = mid

        return left

    def fp_bs(self, left, right):  # => right => previous left result
        while left + 1 < right:
            mid = left + (right-left)//2
            if List[mid][0] == List[right][0]:
                right = mid
            else:
                left = mid

        return right

    def next_envelope(self, fp_idx, lp_idx, prev_env):
        next_env = []
        for i in range(lp_idx, fp_idx-1, -1):
            if List[i][0] < prev_env[0] and List[i][1] < prev_env[1]:
                return list[i]

        return None
