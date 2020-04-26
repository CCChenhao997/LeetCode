'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-26 14:06:24
@LastEditors: chenhao
@LastEditTime: 2020-04-26 14:31:07
'''

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
"""

class Solution:
    def isValid(self, s: str) -> bool:
        stack1 = list(s)
        stack2 = []
        while stack1:
            if not stack2:
                stack2.append(stack1.pop())
            else:
                if self.match(stack1[-1], stack2[-1]):
                    stack1.pop()
                    stack2.pop()
                else:
                    stack2.append(stack1.pop())
        if stack2:
            return False
        return True
                
                
    def match(self, s1, s2):
        if s1 == '(' and s2 == ')':
            return True
        elif s1 == '[' and s2 == ']':
            return True
        elif s1 == '{' and s2 == '}':
            return True
        return False