# Solution
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        prefix = [[0]*26 for _ in range(n+1)]
        for i in range(n):
            for ch in range(26):
                prefix[i+1][ch] = prefix[i][ch]
            idx = ord(s[i]) - ord('a')
            prefix[i+1][idx] += 1
            
        first = [-1] * 26
        last = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if first[idx] == -1:
                first[idx] = i
            last[idx] = i
        
        res = 0
        for x in range(26):
            if first[x] == -1 or first[x] >= last[x]:
                continue
            for y in range(26):
                if prefix[last[x]][y] - prefix[first[x] + 1][y] > 0:
                    res += 1
        return res