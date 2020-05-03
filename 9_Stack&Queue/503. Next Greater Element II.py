'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-03 20:46:57
@LastEditors: chenhao
@LastEditTime: 2020-05-03 21:15:01
'''

"""
Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]

Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.
Note: The length of given array won't exceed 10000.
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        l = len(nums)
        res = [-1] * l
        for i in range(l*2-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % l]:
                stack.pop()
            res[i % l] = -1 if stack == [] else nums[stack[-1]]
            stack.append(i % l)
        return res
        