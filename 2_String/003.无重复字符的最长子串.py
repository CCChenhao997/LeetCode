'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# 解法一: (自己写的) 滑动窗口
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = []
        max_len = 0
        s_len = len(s)
        if s_len == 0:
            return max_len
        for i in range(s_len):
            if s[i] in r:
                r.append(s[i])
                f_index = r.index(s[i])
                r = r[f_index+1:]
            else:
                r.append(s[i])
            if len(r) > max_len:
                max_len = len(r)
        return max_len
"""


# 双指针法 (滑动窗口优化)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串为空则返回零
        if not s:
            return 0
        
        max_length = 0      # 滑动窗口数组
        left, right = 0, 0  # 双指针

        for i, c in enumerate(s):
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in s[left:right]:
                # 右指针右移一位
                right += 1
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 在滑动窗口范围内中找出对应的首个字符的索引X，对应的新的左指针位置为X + 1
                # 左指针右移，索引索引X增一位
                left += s[left:right].index(c) + 1
                # 右指针右移一位
                right += 1
            
            # 更新最大长度
            max_length = max(right - left, max_length)

        # 如果最大长度不为零，返回最大长度
        # 如果最大长度仍为零，则说明遍历整个字符串都没有发现重复字符，最大长度即为字符串本身的长度
        return max_length if max_length != 0 else len(s)



if __name__=='__main__':
    X = Solution()
    s = "abcabcbb"
    print(X.lengthOfLongestSubstring(s))