class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len([1 for i in nums if i % 3 != 0])# Solution
