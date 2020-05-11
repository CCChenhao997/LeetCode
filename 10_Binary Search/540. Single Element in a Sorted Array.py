'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-11 14:23:36
@LastEditors: chenhao
@LastEditTime: 2020-05-11 15:32:44
'''

"""
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once. Find this single element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
"""

from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if left == mid or mid == right:
                break
            # print("left:", left, "mid:", mid, "right:", right)
            if (mid + 1) % 2 == 0: 
                if nums[mid] == nums[mid-1]:
                    left = mid + 1
                    # left = mid
                else:
                    right = mid
            else:
                if nums[mid] != nums[mid-1]:
                    left = mid
                else:
                    right = mid
                             
        return nums[mid]
    

if __name__=='__main__':
    s = Solution()
    test = [1,1,2,3,3]
    print(s.singleNonDuplicate(test))