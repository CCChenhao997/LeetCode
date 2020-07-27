'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-07-27 18:14:48
@LastEditors: chenhao
@LastEditTime: 2020-07-27 18:18:55
'''

"""
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
    The maximum number of consecutive 1s is 3.
    
Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
"""

from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_num, cur_num = 0, 0
        for i in nums:
            cur_num = 0 if i == 0 else cur_num + 1
            max_num = max(max_num, cur_num)
        return max_num