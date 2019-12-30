class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        i, j = 0, 0
        sum = 0

        while j < len(height):
            if j == 0 and height[j] <= height[j+1]:
                j += 1  # j will move to the first edge
                continue
            # if j already at the previous-peak
            elif j < len(height)-1 and height[j] > height[j+1]:
                i = j
                self.findNextPeak(height, j+1, True)
                if j > i+1:
                    self.twoPeakWater(height, i, j, sum)
                    i = j
                    j += 1
                    continue
                else:
                    break
            else:  # not have previous-peak yet
                if j < len(height) - 1:
                    self.findNextPeak(height, j + 1, False)
                    i = j
                else:
                    break
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
        k = start
        if height[start] >= height[end]:
            for k in range(start+1, end):
                if height[end] - height[k] > 0:
                    sum += height[end] - height[k]
                else:
                    continue
        else:
            for k in range(start+1, end):
                if height[start] - height[k] > 0:
                    sum += height[start] - height[k]
                else:
                    break
