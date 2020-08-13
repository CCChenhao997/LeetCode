from typing import List

class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        length = len(A)
        number = 0
        dp = [0] * length
        for i in range(2, length):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                dp[i] = dp[i-1] + 1
                number += dp[i]
        return number
        