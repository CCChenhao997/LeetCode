'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-12 17:01:22
@LastEditors: chenhao
@LastEditTime: 2020-04-12 17:18:14
'''

"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        preSum = nums[0]
        maxSum = preSum
        for i in range(1, len(nums)):
            preSum = preSum + nums[i] if preSum > 0 else nums[i]
            maxSum = max(maxSum, preSum)
        return maxSum