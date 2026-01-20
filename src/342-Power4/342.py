#class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 1:
            return False
        else:
            ans = 1
            while ans <= n:
                if ans == n:
                    return True
                ans <<= 2
            return False Solution
