"""
题目描述:
在一个字符串(0<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置, 如果没有则返回 -1（需要区分大小写）.
"""

class Solution:
    def FirstNotRepeatingChar(self, s):
        if s == None or len(s) <= 0:
            return -1
        Hash = {}
        for i in s:
            Hash.update({i: Hash.get(i, 0)+1})
        for index, key in enumerate(s):
            if Hash[key] == 1:
                return index
        return -1


s = Solution()
print(s.FirstNotRepeatingChar('abaccdeff'))