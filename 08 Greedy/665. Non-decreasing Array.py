'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-11 17:04:49
@LastEditors: chenhao
@LastEditTime: 2020-04-11 17:39:19
'''

"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

Example 1:
Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.

Constraints:
1 <= n <= 10 ^ 4
- 10 ^ 5 <= nums[i] <= 10 ^ 5
"""

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        tolerance = 1
        for i in range(1, len(nums)):
            if nums[i-1] <= nums[i]:
                continue
            
            if i >= 2 and nums[i-2] > nums[i]:
                nums[i] = nums[i-1]
            else:
                nums[i-1] = nums[i]
                    
            tolerance -= 1
            if tolerance < 0:
                return False
        return True