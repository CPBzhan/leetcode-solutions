class Solution:
    def maxSubarraySum(self, nums, k):
        n = len(nums)
        prefix = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        ans = -10**18

        for r in range(k):  # 0..k-1
            min_prefix = 10**18

            # 枚举所有下标 i 满足 i % k == r
            for i in range(r, n + 1, k):
                ans = max(ans, prefix[i] - min_prefix)
                min_prefix = min(min_prefix, prefix[i])

        return ans