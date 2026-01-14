# Solution
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        cnt = 0
        n = len(strs[0])
        for i in range(n):
            for j in range(len(strs) - 1):
                if ord(strs[j][i]) > ord(strs[j+1][i]):
                    cnt += 1
                    break
        return cnt
