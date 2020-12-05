'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-29 17:40:57
@LastEditors: chenhao
@LastEditTime: 2020-07-29 20:23:30
'''

"""
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of the numbers in the set got duplicated to another number in the set, which results in repetition of one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]

Note:
The given array size will in the range [2, 10000].
The given array's numbers won't have any order.
"""

from typing import List

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return None
        
        repNum, lostNum = None, None
        numsDict = {}
        for key in range(1, len(nums) + 1):
            numsDict[key] = 0
        
        for i in nums:
            numsDict[i] += 1
            if numsDict[i] > 1:
                repNum = i
                
        for num in range(1, len(nums) + 1):
            if numsDict[num] == 0:
                lostNum = num
                break
        
        return [repNum, lostNum]