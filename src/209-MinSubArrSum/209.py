class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        sum1 = l = 0
        n = len(nums)
        ans = 10**5 + 1

        for r in range(n):
            sum1 += nums[r]
            while sum1 >= target:
                ans = min(ans, r - l + 1)
                sum1 -= nums[l]
                l += 1

        return 0 if ans == 10**5 + 1 else ans
