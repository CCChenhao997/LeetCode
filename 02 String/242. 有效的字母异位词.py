'''
Description: 
version: 
Author: chenhao
Date: 2021-01-27 23:24:31
'''

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:
输入: s = "anagram", t = "nagaram"
输出: true

示例 2:
输入: s = "rat", t = "car"
输出: false

说明:
你可以假设字符串只包含小写字母。

进阶:
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashtable = {}
        for i in s:
            hashtable[i] = hashtable.get(i, 0) + 1
        for j in t:
            if j not in hashtable or hashtable[j] == 0:
                return False
            hashtable[j] -= 1
        return True
    

if __name__ == '__main__':
    print(ord('A'))
    print(chr(65))