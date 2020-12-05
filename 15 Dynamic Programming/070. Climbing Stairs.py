
class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        # dp = [0]*n
        # dp[0] = 1
        # dp[1] = 2
        # for i in range(2, n):
        #     dp[i] = dp[i-1] + dp[i-2]
        # return dp[n-1]
        
        a, b = 1, 2
        for i in range(3, n+1):
            t = b
            b = a + b
            a = t
        return b