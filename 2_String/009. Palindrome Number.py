'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-06-19 20:42:56
@LastEditors: chenhao
@LastEditTime: 2020-06-19 20:57:41
'''

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:
Input: 121
Output: true

Example 2:
Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:
Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        str_x = str(x)
        left, right = 0, len(str_x) - 1
        while left < right:
            if str_x[left] != str_x[right]:
                return False
            left += 1
            right -= 1
        return True
    
    def isPalindrome_without_string(self, x: int) -> bool:
        if x < 0:
            return False
        a, b = x, 0
        while a > 0:
            b = b * 10 + a % 10
            a //= 10
        return x == b