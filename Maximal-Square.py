class Solution(object):
    def maximalSquare(self, matrix):
        \\\
        :type matrix: List[List[str]]
        :rtype: int
        \\\
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dp = [[0]*n for _ in range(m)]
        max_side = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        dp[i][j] = 1  # edges
                    else:
                        dp[i][j] = 1 + min(
                            dp[i-1][j],     # top
                            dp[i][j-1],     # left
                            dp[i-1][j-1]    # top-left
                        )
                    max_side = max(max_side, dp[i][j])

        return max_side * max_side  # area
