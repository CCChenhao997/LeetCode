"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Input: "hello"
Output: "holle"

Example 2:
Input: "leetcode"
Output: "leotcede"

Note:
The vowels does not include the letter "y".
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        sList = list(s)
        low, high = 0, len(sList) - 1
        vowelsList = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while low < high:
            while sList[low] not in vowelsList and low < high:
                low += 1
            while sList[high] not in vowelsList and low < high:
                high -= 1
            if low < high:
                sList[low], sList[high] = sList[high], sList[low]
                low += 1
                high -= 1
        return ''.join(sList)
    

s = Solution()
print(s.reverseVowels("leetcode"))