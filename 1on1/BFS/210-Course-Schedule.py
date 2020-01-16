import queue


class Solution:
    def findOrder(self, numCourses: int, pre: List[List[int]]) -> List[int]:
        if numCourses <= 1 or not pre:
            return numCourses
