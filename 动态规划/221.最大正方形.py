"""
在一个由 '0' 和 '1' 组成的二维矩阵内，找到只包含 '1' 的最大正方形，并返回其面积。
"""


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # 使用动态规划
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        # dp = [[0 for _ in range(n)] for _ in range(m)]
        max_len = 0
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if not i or not j or matrix[i][j] == '0':
                    dp[i][j] = 0 if matrix[i][j] == '0' else 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1])) + 1
                max_len = max(max_len, dp[i][j])
        return max_len ** 2



