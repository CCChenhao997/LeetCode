"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5
 

Example 2:
Input: 3
Output: False
"""

import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        low, high = 0, int(math.sqrt(c))
        while low <= high:
            res = low*low + high*high
            if res == c:
                return True
            elif res > c:
                high -= 1
            else:
                low += 1
        return False
    

s = Solution()
print(s.judgeSquareSum(2))