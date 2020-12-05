"""
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
 
Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
 
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # n = len(nums)
        # target = sum(nums)
        # if target % 2 != 0:
        #     return False
        # target //= 2
        # dp = [[False] * (target + 1) for _ in range(n)]
        # dp[0][0] = True
        # for i in range(1, target + 1):
        #     if nums[0] == i:
        #         dp[0][i] = True
        #         break
        # for i in range(1, n):
        #     for j in range(target + 1):
        #         if j >= nums[i]:
        #             dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
        #         else:
        #             dp[i][j] = dp[i-1][j]
        # return dp[-1][-1]
        
        # * 空间优化
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        pre = [False] * (target + 1)
        cur = [False] * (target + 1)
        pre[0] = True
        for i in range(1, target + 1):
            if nums[0] == i:
                pre[i] = True
                break
        for i in range(1, n):
            for j in range(target + 1):
                if j >= nums[i]:
                    cur[j] = pre[j] or pre[j-nums[i]]
                else:
                    cur[j] = pre[j]
            pre = cur[:]
        return cur[-1]