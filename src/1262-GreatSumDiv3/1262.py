from typing import List

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # dp[r] 表示当前总和模3余r的最大和
        dp = [0, -10**9, -10**9]
        for num in nums:
            current_dp = dp.copy()
            for r in range(3):
                if current_dp[r] != -10**9:
                    # 计算加上当前数字后的新余数
                    new_r = (r + num) % 3
                    # 更新新余数状态的最大和
                    dp[new_r] = max(dp[new_r], current_dp[r] + num)
        return dp[0]# Solution
