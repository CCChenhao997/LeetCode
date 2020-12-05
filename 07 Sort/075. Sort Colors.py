"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
    A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
    Could you come up with a one-pass algorithm using only constant space?
"""

from typing import List

class Solution:
    
    # two-pass
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        num_0, num_1, num_2 = 0, 0, 0
        for val in nums:
            if val == 0:
                num_0 += 1
            elif val == 1:
                num_1 += 1
            else:
                num_2 += 1
 
        for i in range(len(nums)):
            if i >= 0 and i < num_0:
                nums[i] = 0
            elif i >= num_0 and i < num_1 + num_0:
                nums[i] = 1
            else:
                nums[i] = 2
    
    
    
    # one-pass and three pointers
    def sortColors2(self, nums: List[int]) -> None:
        p0 = curr = 0
        p2 = len(nums) - 1
        
        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                curr += 1
                p0 += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[p2], nums[curr] = nums[curr], nums[p2]
                p2 -= 1
        
        # return nums
                  

s = Solution()
print(s.sortColors3([1, 0, 2, 0, 1]))