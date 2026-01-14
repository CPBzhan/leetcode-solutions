# Solution
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        cnt = 0
        for i in range(len(grid)):
            for j in range(n - 1, -1, -1):
                if grid[i][j] < 0: cnt += 1
                else: break
        return cnt
