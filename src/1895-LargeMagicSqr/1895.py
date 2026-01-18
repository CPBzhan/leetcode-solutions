# Solution
class Solution:
    def largestMagicSquare(self, grid):
        n, m = len(grid), len(grid[0])

        # 行前缀和
        row = [[0]*(m+1) for _ in range(n)]
        for i in range(n):
            for j in range(m):
                row[i][j+1] = row[i][j] + grid[i][j]

        # 列前缀和
        col = [[0]*(n+1) for _ in range(m)]
        for j in range(m):
            for i in range(n):
                col[j][i+1] = col[j][i] + grid[i][j]

        max_k = min(n, m)

        for k in range(max_k, 1, -1):
            for i in range(n - k + 1):
                for j in range(m - k + 1):
                    target = row[i][j+k] - row[i][j]

                    ok = True
                    # 行
                    for r in range(i, i+k):
                        if row[r][j+k] - row[r][j] != target:
                            ok = False
                            break

                    # 列
                    for c in range(j, j+k):
                        if col[c][i+k] - col[c][i] != target:
                            ok = False
                            break

                    # 主对角线
                    d1 = sum(grid[i+t][j+t] for t in range(k))
                    d2 = sum(grid[i+t][j+k-1-t] for t in range(k))

                    if d1 != target or d2 != target:
                        ok = False

                    if ok:
                        return k

        return 1
