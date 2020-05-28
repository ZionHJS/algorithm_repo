class Solution:
    def medianSlidingWindow(self, N: List[int], k: int) -> List[float]:
        if not N or k <= 0:
            return []
        res = []
        # build the first sorted window
        window = N[:k][:]
        window.sort()  # O(klogk)

        # loop through N  => O(k*N)
        for i in range(k, len(N)+1):
            # update res
            if k % 2:
                res.append(window[len(window)//2])
            else:
                res.append((window[len(window)//2-1] +
                            window[len(window)//2])/2)
            if i == len(N):
                break
            # update window
            re_idx = window.index(N[i-k])  # 这步骤可以省略
            window[re_idx] = N[i]
            while (0 <= re_idx <= len(window)-1):
                if re_idx > 0 and window[re_idx] < window[re_idx-1]:
                    window[re_idx], window[re_idx -
                                           1] = window[re_idx-1], window[re_idx]
                    re_idx -= 1
                elif re_idx < len(window)-1 and window[re_idx] > window[re_idx+1]:
                    window[re_idx], window[re_idx +
                                           1] = window[re_idx+1], window[re_idx]
                    re_idx += 1
                else:
                    break

        return res
