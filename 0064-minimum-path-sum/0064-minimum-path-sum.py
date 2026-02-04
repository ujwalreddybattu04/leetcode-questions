class Solution:
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Create DP table
        dp = [[0] * n for _ in range(m)]

        # Starting cell
        dp[0][0] = grid[0][0]

        # Fill first row
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1] + grid[0][j]

        # Fill first column
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0] + grid[i][0]

        # Fill rest of the dp table
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

        return dp[m - 1][n - 1]
