# Solution
class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        n = len(mat)
        m = len(mat[0])
        pre = [[0] * (m+1) for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1, m+1):
                pre[i][j] = pre[i-1][j] + pre[i][j-1] - pre[i-1][j-1] + mat[i-1][j-1]
        
        left, right = 0, min(n, m)
        ans = 0

        while left < right:
            mid = (left + right + 1) // 2
            flag = False

            for i in range(mid, n+1):
                for j in range(mid, m+1):
                    psum = (pre[i][j] - pre[i-mid][j] - pre[i][j-mid] + pre[i-mid][j-mid])
                    if psum <= threshold:
                        ans = mid
                        flag = True
                        break
                if flag:
                    break

            if flag:
                left = mid
            else:
                right = mid - 1

        return ans
