# Solution
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        lo = float('inf')
        hi = float('-inf')
        total = 0.0

        for x, y, l in squares:
            total += l * l
            lo = min(lo, y)
            hi = max(hi, y + l)

        target = total / 2.0

        def area_below(Y: float) -> float:
            s = 0.0
            for _, y, l in squares:
                h = Y - y
                if h <= 0:
                    continue
                if h >= l:
                    s += l * l
                else:
                    s += l * h
            return s

        # 二分找最小 y，使 area_below(y) >= target
        for _ in range(70):  # 60~80 都行，70 更稳
            mid = (lo + hi) / 2.0
            ca = area_below(mid)
            if ca >= target:
                hi = mid
            else:
                lo = mid

        return hi
