"""
You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
Find out how many ways to assign symbols to make sum of integers equal to target S.

Example 1:
Input: nums is [1, 1, 1, 1, 1], S is 3. 
Output: 5

Explanation: 
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

There are 5 ways to assign symbols to make the sum of nums be target 3.
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        sumN = sum(nums)
        
        # 背包容量为整数，sum+S为奇数的话不满足要求 or 目标和不可能大于总和
        if (sumN + S) % 2 == 1 or S > sumN:
            return 0
        
        lenN = (sumN + S) // 2
        dp = [0] * (lenN + 1)
        dp[0] = 1
        
        for num in nums:
            for i in range(lenN, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[lenN]
                
        
s = Solution()
print(s.findTargetSumWays([1,1,1,1,1], 3))   