class Solution:
    def intersectionSizeTwo(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x : x[1])
        ans = 0
        cur = []
        for s, e in intervals:
            if not cur or s > cur[1]:
                ans += 2
                cur = [e-1, e]
            elif s > cur[0]:
                ans += 1
                if cur[1] == e:
                    cur = [e-1, e]
                else:
                    cur = [cur[1], e]
        return ans# Solution
