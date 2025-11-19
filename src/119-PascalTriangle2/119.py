class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        t = []
        for i in range(rowIndex + 1):
            row = [1] * (i+1)
            for j in range(1,i):
                row[j] = t[i - 1][j - 1] + t[i-1][j]
            t.append(row)
        return t[rowIndex]# Solution
