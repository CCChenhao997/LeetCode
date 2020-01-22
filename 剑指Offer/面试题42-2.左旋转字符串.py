"""
题目描述:
字符串的左旋转操作就是把字符串前面的若干个字符转移到字符串的尾部。
请定义一个函数实现字符串左旋转操作的功能。比如输入字符串"abcdefg"和
数字2，该函数将返回左旋转2位得到的结果"cdefgab"。

思路:
首先需要写一个reverse函数，把任何输入的字符串完全翻转。然后根据题目中给出的左旋转字符串的个数n，
用全字符串长度length减去旋转字符串个数n，求得对于新的字符串应该在哪一位进行旋转，然后分别旋转前
[:length-n]子串和[length-n:]子串，重新拼接两个子串即可。
"""

class Solution:
    def LeftRotateString(self, s, n):
        if len(s) <= 0 or len(s) < n or n < 0:
            return ''
        strList = list(s)
        self.Reverse(strList)
        length = len(s)
        pivot = length - n
        frontList = self.Reverse(strList[:pivot])
        behindList = self.Reverse(strList[pivot:])
        resultStr = ''.join(frontList) + ''.join(behindList)
        return resultStr
    
    def Reverse(self, alist):
        if alist == None or len(alist) <= 0:
            return ''
        startIndex = 0
        endIndex = len(alist) - 1
        while startIndex < endIndex:
            alist[startIndex], alist[endIndex] = alist[endIndex], alist[startIndex]
            startIndex += 1
            endIndex -= 1
        return alist
    
    
test = 'abcdefg'
s = Solution()
print(s.LeftRotateString(test, 2))