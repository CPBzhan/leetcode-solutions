# Solution
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = []
        carry = 0
        i, j = len(a)-1, len(b)-1

        while i >= 0 or j >= 0 or carry:
            carry += (a[i] == '1') if i >= 0 else 0
            carry += (b[j] == '1') if j >= 0 else 0
            res.append(str(carry & 1))
            carry >>= 1
            i -= 1
            j -= 1

        return ''.join(reversed(res))
