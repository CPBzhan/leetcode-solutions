class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        res = set()
        cur = set()

        for a in arr:
            new_cur = {a}
            for x in cur:
                new_cur.add(x | a)

            cur = new_cur
            res |= cur

        return len(res)# Solution
