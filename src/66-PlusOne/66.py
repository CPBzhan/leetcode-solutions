# Solution
from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for n in digits:
            s += str(n)
        ans = str(int(s) + 1)
        return [int(ch) for ch in ans]
