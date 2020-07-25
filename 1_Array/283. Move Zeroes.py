'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-25 18:26:27
@LastEditors: chenhao
@LastEditTime: 2020-07-25 18:48:28
'''

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = 0
        for value in nums:
            if value != 0:
                nums[idx] = value
                idx += 1
        for i in range(idx, len(nums)):
            nums[i] = 0
