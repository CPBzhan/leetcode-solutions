# Solution
class Solution:
    def maximizeSquareArea(self, m: int, n: int,
                           hFences: List[int],
                           vFences: List[int]) -> int:
        MOD = 10**9 + 7

        hf = hFences + [1, m]
        vf = vFences + [1, n]

        hf.sort()
        vf.sort()

        set_h = set()
        for i in range(len(hf)):
            for j in range(i+1, len(hf)):
                set_h.add(hf[j] - hf[i])

        set_v = set()
        for i in range(len(vf)):
            for j in range(i+1, len(vf)):
                set_v.add(vf[j] - vf[i])

        common = set_h & set_v
        if not common:
            return -1

        side = max(common)
        return (side * side) % MOD
