'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-06-12 16:20:19
@LastEditors: chenhao
@LastEditTime: 2020-06-12 20:58:02
'''

"""
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        hash_dict = {}
        for i in range(len(s)):
            if s[i] not in hash_dict:
                if t[i] in hash_dict.values():
                    return False
                else:
                    hash_dict[s[i]] = t[i]
            else:
                if hash_dict[s[i]] != t[i]:
                    return False
        return True
                