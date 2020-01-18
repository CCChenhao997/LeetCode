"""
题目描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。

思路：
空间换时间。建立一个长度为n的数组，保存这n个丑数。在进行运算的时候，某个位置需要求得丑数一定是前面
某个丑数乘以2、3或者5的结果，我们分别记录之前乘以2后能得到的最大丑数M2，乘以3后能得到的最大丑数M3，
乘以5后能得到的最大丑数M5，那么下一个丑数一定是M2，M3，M5中的最小的那一个。同时注意到，已有的丑数
是按顺序存放在数组中的。对乘以2而言，肯定存在某一个丑数T2，排在他之前的每一个丑数乘以2得到的结果都
会小于已有的最大丑数，在他之后的每一个丑数乘以2得到的结果都会太大，我们只需记下这个丑数的位置，每次
生成新的丑数的时候，去更新这个T2。对于3和5同理。
"""


class Solution:
    def GetUglyNumber_Solution(self, index):
        if index == None or index <= 0:
            return 0
        uglyNumbers = [1]*index
        nextIndex = 1
        index2 = 0
        index3 = 0
        index5 = 0
        while nextIndex < index:
            minVal = min(uglyNumbers[index2]*2, uglyNumbers[index3]*3, uglyNumbers[index5]*5)
            uglyNumbers[nextIndex] = minVal
            while uglyNumbers[index2]*2 == uglyNumbers[nextIndex]:
                index2 += 1
            while uglyNumbers[index3]*3 == uglyNumbers[nextIndex]:
                index3 += 1
            while uglyNumbers[index5]*5 == uglyNumbers[nextIndex]:
                index5 += 1
            nextIndex += 1
        return uglyNumbers[-1]
    
    
s = Solution()
print(s.GetUglyNumber_Solution(11))        