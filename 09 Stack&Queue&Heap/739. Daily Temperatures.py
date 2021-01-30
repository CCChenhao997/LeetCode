'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-27 18:16:00
@LastEditors: chenhao
@LastEditTime: 2020-04-27 20:11:15
'''

"""
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100].
"""

from typing import List

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        res = [0] * len(T)
        for i, num in zip(range(len(T)-1, -1, -1), T[::-1]):
            while stack and T[stack[-1]] <= num:
                stack.pop()
            if stack:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
        
    

s = Solution()
print(s.dailyTemperatures([1, 2, 3, 0]))
            