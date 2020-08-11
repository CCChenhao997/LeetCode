
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        # Memory O(n2)
        # dp = [[0 for j in range(n)] for i in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 or j == 0: dp[i][j] = 1
        #         else: dp[i][j] = dp[i][j-1] + dp[i-1][j]
        
        # return dp[-1][-1]

        # Memory O(n)
        cur = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j-1]
        return cur[-1]