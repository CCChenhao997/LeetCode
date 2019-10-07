'''
题目描述:
请实现一个函数，将一个字符串中的每个空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。

书中思路:
如果直接每次遇到空格添加'%20'，那么空格后面的数字就需要频繁向后移动。
遇到这种移动问题，我们可以尝试先给出最终需要的长度，然后从后向前扫描，
同时给定两个指针来保证定位。
'''

class Solution:
    # s 源字符串

    # 书中的思路
    # 判断输入类型的时候，isinstance必须首先判断，因为如果输入为integer的话，没有len，就会直接报错
    def replaceSpace(self, s):
        if not isinstance(s, str) or len(s) <= 0 or s == None:
            return ''
        spaceNum = 0
        # 计算空格的数量
        for i in s:
            if i == ' ':
                spaceNum += 1

        newStrlen = len(s) + spaceNum * 2
        newStr = newStrlen * [None]
        indexOfOriginal, indexOfNew = len(s) - 1, newStrlen - 1
        while indexOfNew >= 0 and indexOfNew >= indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew-2:indexOfNew+1] = ['%', '2', '0']
                indexOfNew -= 3
                indexOfOriginal -= 1
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
                indexOfOriginal -= 1
        return ''.join(newStr)


    # 使用replace内置函数
    def replaceSpace1(self, s):
        return s.replace(' ', '%20')


    # 使用正则表达式
    def replaceSpace2(self, s):
        import re
        ret = re.compile(' ')
        return ret.sub('%20', s)


    # 使用append一次遍历即可替换
    # 由于list的append是O(1)的时间复杂度，除了扩容所导致的时间损耗，该算法复杂度为O(n)
    def replaceSpace3(self, s):
        s = list(s)
        sReplace = []
        for item in s:
            if item == ' ':
                sReplace.append('%')
                sReplace.append('2')
                sReplace.append('0')
            else:
                sReplace.append(item)
        return ''.join(sReplace)


    # 创建新的字符串进行替换，思路跟上面replaceSpace3差不多
    def replaceSpace4(self, s):
        tempstr = ''
        if type(s) != str:
            return
        for c in s:
            if c == ' ':
                tempstr += '%20'
            else:
                tempstr += c
        return tempstr

