class Solution:
    def __init__(self):
        self.room_list = []

    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        n = len(intervals)
        target = intervals[-1]
        self.room_list.append([target])

        self.partition(intervals, target)

        print("room_list:", self.room_list)
        return len(self.room_list)

    def partition(self, intervals, target):
        if not intervals:
            return

        for event in intervals:
            if not self.confOrNot(target, event):
                # intervals.remove(event)
                self.room_list[-1].append(event)

        for event in self.room_list[-1]:
            if event in intervals:
                intervals.remove(event)

        print("intervals:", intervals)

        if len(intervals) > 0:
            target = intervals[-1]
            self.room_list.append([target])
        else:
            return

        if len(intervals) > 0:
            self.partition(intervals, target)

        return

    def confOrNot(self, arr1, arr2):
        if arr2[0] >= arr1[1] or arr2[1] <= arr1[0]:
            return False
        else:
            return True
