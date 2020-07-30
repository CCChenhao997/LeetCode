'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-30 10:40:36
@LastEditors: chenhao
@LastEditTime: 2020-07-30 11:20:19
'''

"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        size = len(nums)
        left = 1
        right = size - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            cnt = 0
            for num in nums:
                if num <= mid:
                    cnt += 1
                    
            if cnt > mid:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    
    def findDuplicate_pointer(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        root = 0
        while root != slow:
            root = nums[root]
            slow = nums[slow]
        return slow