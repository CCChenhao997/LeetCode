'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-27 21:51:40
@LastEditors: chenhao
@LastEditTime: 2020-05-27 22:01:10
'''

"""
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:
Input: [1,2,3,1]
Output: true

Example 2:
Input: [1,2,3,4]
Output: false

Example 3:
Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hash_dict = {}
        for i, v in enumerate(nums):
            if not hash_dict.get(v):
                hash_dict[v] = i
        return False if len(nums) == len(hash_dict) else True
        

s = Solution()
print(s.containsDuplicate([1, 1, 2, 3]))