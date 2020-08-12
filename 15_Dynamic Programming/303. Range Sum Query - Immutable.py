"""
Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

Example:
Given nums = [-2, 0, 3, -5, 2, -1]
sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
 
Constraints:
You may assume that the array does not change.
There are many calls to sumRange function.
0 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
0 <= i <= j < nums.length
"""

from typing import List
import copy

class NumArray:

    def __init__(self, nums: List[int]):
        length = len(nums)
        # self.dp = [copy.deepcopy(nums) for i in range(length)]
        # for i in range(length):
        #     for j in range(length):
        #         if j <= i: continue
        #         self.dp[i][j] = self.dp[i][j-1] + self.dp[i][j]
        self.dp = [0] * length
        for i in range(length):
            if i == 0:
                self.dp[i] = nums[i]
            else:
                self.dp[i] = self.dp[i - 1] + nums[i]
                
    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.dp[j]
        else:
            return self.dp[j] - self.dp[i-1]
    

s = NumArray([-2, 0, 3, -5, 2, -1])
print(s.sumRange(2, 5))