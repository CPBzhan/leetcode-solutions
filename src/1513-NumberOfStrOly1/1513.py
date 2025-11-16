# Solution
class Solution:
    def numSub(self, s: str) -> int:
        ones = [i for i in s.split('0') if s != '']
        ans = anss = 0
        MOD = 10**9 + 7
        for n in ones:
            for i in range(len(n)):
                if len(n) - i > 0:
                    ans += len(n) - i
                else: continue
            anss += ans
            ans = 0
        return anss % MOD