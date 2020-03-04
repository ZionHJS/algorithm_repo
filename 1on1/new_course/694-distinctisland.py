import queue


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
