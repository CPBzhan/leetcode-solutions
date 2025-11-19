def generate(numRows):
    triangle = []

    for i in range(numRows):
        # 每一行先放全是 1 的初始结构
        row = [1] * (i + 1)

        # 中间的数字从上一行相加得到
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

        triangle.append(row)

    return triangle# Solution
