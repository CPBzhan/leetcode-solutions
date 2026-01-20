#class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0:
            return t
        ss = [ord(i) for i in s]
        tt = [ord(i) for i in t]
        ans = 0
        for c in ss:
            ans ^= c
        for c in tt:
            ans ^= c
        return chr(ans)
         Solution
