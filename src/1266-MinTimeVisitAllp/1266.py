# Solution
class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        score = 0
        for i in range(len(points) - 1):
            start = points[i]
            end = points[i+1]
            dx = abs(start[0] - end[0])
            dy = abs(start[1] - end[1])
            score += min(dx, dy) + abs(dy - dx)
        return score

