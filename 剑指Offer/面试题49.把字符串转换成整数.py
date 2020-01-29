"""
题目描述：
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。
数值为0或者字符串不是一个合法的数值则返回0

思路：
主要是区分输入和合法性，比如输入一个None，输入一个空字符串 ""，
或者输入的字符串中含有“+”或者“-”，或者输入的字符串中含有除去+ — 
数字的非数字字符，如何段应正常的输出还是报错，需要考虑的全面一些。
"""

class Solution:
    def StrToInt(self, s):
        if not s or s == '+' or s == '-':
            return 0
        flag = s[0]
        # 首个字符为数字时，计算值，并将flag设为正
        if flag <= '9' and flag >= '0':
            sum1 = int(s[0]) * 10 ** (len(s)-1)
            flag = '+'
        elif flag in ['+', '-']:
            sum1 = 0
        # 异常，返回0
        else:
            return 0
        for i in range(1, len(s)):
            if s[i] > '9' or s[i] < '0':
                return 0
            sum1 += int(s[i]) * 10 ** (len(s)-1-i)
        # 判断取值范围是否合法
        if flag == '+' and sum1 > 0x7FFFFFFF:
            return 0
        if flag == '-' and sum1 > 0x80000000:
            return 0
        return sum1 if flag == '+' else -sum1
    
    
test = '-2147483649'
s = Solution()
print(s.StrToInt(test))