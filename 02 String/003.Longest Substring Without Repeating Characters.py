"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        alist = list(s)
        windowSize, maxSize = 1, 1
        windowSizeList = alist[0 : 1]
        for i in range(1, len(alist)):
            if alist[i] not in windowSizeList:
                windowSizeList.append(alist[i])
                windowSize += 1
                if maxSize < windowSize:
                    maxSize = windowSize
            else:
                start = 1
                while alist[i] in windowSizeList[start:]:
                    windowSize -= 1
                    start += 1
                windowSizeList = windowSizeList[start:]
                windowSizeList.append(alist[i])
            # print(windowSizeList)
        return maxSize
        

s = Solution()
print(s.lengthOfLongestSubstring("ohvhjdml"))
print(s.lengthOfLongestSubstring("pwwkew"))