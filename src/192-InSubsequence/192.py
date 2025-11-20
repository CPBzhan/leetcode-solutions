class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        dp = [[False for _ in range(len(t)+1)] for _ in range(len(s)+1)]
        dp[0] = [True for _ in range(len(t)+1)]
        for i in range(1, len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else: dp[i][j] = dp[i][j-1]
        return dp[len(s)][len(t)]
'''
        ""   a   h   b   g   d   c
      --------------------------------
"" |    T    T   T   T   T   T   T
a  |    F    T   T   T   T   T   T
b  |    F    F   F   T   T   T   T
c  |    F    F   F   F   F   F   T
'''# Solution
