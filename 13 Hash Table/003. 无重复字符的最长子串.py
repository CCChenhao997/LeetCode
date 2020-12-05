'''
Description: 
version: 
Author: chenhao
Date: 2020-12-02 20:12:06
'''

"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

示例 4:
输入: s = ""
输出: 0

提示：
0 <= s.length <= 5 * 104
s 由英文字母、数字、符号和空格组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s or len(s) == 0:
            return 0
        begin, end = 0, 0
        max_len = 1
        res = dict()
        for end in range(len(s)):            
            if end == 0:
                res[s[end]] = 1
            else:
                res[s[end]] = res.get(s[end], 0) + 1
                if max_len < len(res):
                    max_len = len(res)
                while len(res) != (end - begin + 1):
                    if res[s[begin]] == 1:
                        res.pop(s[begin])
                    else:
                        res[s[begin]] -= 1
                    begin += 1
            
        return max_len
    
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s or len(s) == 0:
    #         return 0
    #     begin, end = 0, 0
    #     max_len = 1
    #     while end < len(s) - 1:
    #         tmp_len = len(set(s[begin: end + 1]))
    #         if tmp_len == (end - begin + 1):
    #             if max_len < tmp_len:
    #                 max_len = tmp_len
    #             end += 1
    #         else:
    #             begin += 1
        
    #     return max_len


s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))