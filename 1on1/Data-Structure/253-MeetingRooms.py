class Solution:
    def __init__(self):
        self.room_list = [[]]

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        n = len(intervals)
        target = intervals.pop()

        self.partition(intervals, target)

        if len(self.room_list[-1]) > 0:
            return len(self.room_list)
        else:
            return len(self.romm_list) - 1

    def partition(self, intervals, target):
        if not intervals:
            return

        for i in range(len(intervals)):
            if len(intervals) > 0:
                if not self.confOrNot(target, intervals[i]):
                    self.room_list[-1].append(intervals.pop(i))
            else:
                return

        if len(intervals) > 0:
            target = intervals.pop()
            self.room_list.append([])
        else:
            return

        if len(intervals) > 0:
            self.partition(intervals, target)

        return

    def confOrNot(self, arr1, arr2):
        if (arr2[0] >= arr1[0] and arr2[0] < arr[1]) or (arr2[1] > arr1[0] and arr2[1] <= arr1[1]):
            return True
        else:
            return False
