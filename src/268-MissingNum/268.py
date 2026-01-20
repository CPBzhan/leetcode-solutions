#class Solution:
    def missingNumber(self, nums):
        n = len(nums)
        ans = 0

        for i in range(n + 1):
            ans ^= i

        for x in nums:
            ans ^= x

        return ans Solution
