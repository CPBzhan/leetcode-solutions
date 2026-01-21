#class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        a = 
        for n in nums:
            a.append(-1) if n == 2 else a.append(n - ((n + 1) & (-n - 1)) // 2)
        return a
             Solution
