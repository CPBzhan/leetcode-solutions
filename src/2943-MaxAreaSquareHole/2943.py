# Solution
class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        sh = sorted(hBars)
        sv = sorted(vBars)

        # 横向
        curh = maxh = 1
        for i in range(len(sh) - 1):
            if sh[i+1] == sh[i] + 1:
                curh += 1
            else:
                maxh = max(maxh, curh)
                curh = 1
        maxh = max(maxh, curh)

        # 纵向
        curv = maxv = 1
        for i in range(len(sv) - 1):
            if sv[i+1] == sv[i] + 1:
                curv += 1
            else:
                maxv = max(maxv, curv)
                curv = 1
        maxv = max(maxv, curv)

        side = min(maxh + 1, maxv + 1)
        return side * side
