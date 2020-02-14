"""
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
"""

class Solution:
    def validPalindrome(self, s: str) -> bool:
        sList = list(s)
        low, high = 0, len(sList) - 1
        while low < high:
            if sList[low] != sList[high]:
                return self.judePalindrome(sList, low, high-1) or self.judePalindrome(s, low+1, high)
            low += 1
            high -= 1
        return True
        
    def judePalindrome(self, sList, low, high):
        while low <= high:
            if sList[low] != sList[high]:
                return False
            low += 1
            high -= 1
        return True

s = Solution()
print(s.validPalindrome("abbca"))