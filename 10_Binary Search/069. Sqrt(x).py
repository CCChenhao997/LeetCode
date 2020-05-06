'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-05-06 21:29:30
@LastEditors: chenhao
@LastEditTime: 2020-05-06 21:52:04
'''

"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r = 0, x
        while l <= r:
            c = l + (r - l) // 2
            if c**2 <= x and (c+1)**2 > x:
                return c
            elif c**2 > x:
                r = c - 1
            else:
                l = c + 1