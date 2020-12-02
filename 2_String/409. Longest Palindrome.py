'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-06-11 10:11:44
@LastEditors: chenhao
@LastEditTime: 2020-06-11 10:29:32
'''

"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for char in s:
            if char in count:
                count[char] += 1
            else:
                count[char] = 1
        
        ans, odd = 0, 0        
        for value in count.values():
            if value % 2 != 0:
                odd = 1
            if value % 2 == 0:
                ans += value
            elif value > 1:
                ans += (value - 1)

        return ans + odd
    
    def longestPalindrome_(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans