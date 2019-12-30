class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        down = True
        i, j = 0, 0
        sum = 0

        while j < len(height):
            # find the first-peak j => must be the first-peak
            if j == 0 and height[j] <= height[j+1]:
                j += 1
                continue
            else:
                i = j
                if j+1 < len(height):
                    self.findNextPeak(height, j+1, down)
                    if j > i+1:
                        self.twoPeakWater(height, i, j, sum)
                        i = j
                        j += 1
                        continue
                else:
                    pass

            j += 1

        return sum

    # passing down = True, j-1 must be the previous peak
    def findNextPeak(self, height, j, down):
        start_j = j

        while j < len(height):
            if down and height[j] > height[j-1]:
                down = False
            elif down == False and height[j] < height[j-1]:
                down = True
                j = j - 1  # j-1 => nextpeak
                break
            j += 1

        if down == False and j >= len(height):
            j = len(height) - 1  # len-1 => nextpeak
        elif down == True and j >= len(height):
            j = start_j  # no nextpeak find

    def twoPeakWater(self, height, start, end, sum):
        peak_sum = 0
        k = start
        if height[start] >= height[end]:
            for k in range(start+1, end):
                if height[end] - height[k] > 0:
                    peak_sum += height[end] - height[k]
        else:
            for k in range(start+1, end):
                if height[start] - height[k] > 0:
                    peak_sum += height[start] - height[k]
                else:
                    break

        sum += peak_sum
