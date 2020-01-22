"""
题目描述：
找出所有和为S的连续正数序列
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序

思路：
设定两个指针，先分别指向数字1和数字2，并设这两个指针为small和big，对small和big求和，
如果和大于目标值，则从当前和中删除small值，并把small值加一，如果和小于目标值，则把big值加一，
再把新的big值加入和中。如果和等于目标值，就输出small到big的序列，同时把big加一并加入和中，继续之前的操作。
"""

class Solution:
    def FindContinuousSequence(self, tsum):
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) // 2
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big+1)))
            while curSum > tsum and small < middle:
                curSum -= small
                small += 1
                if curSum == tsum:
                    output.append(list(range(small, big+1)))
            big += 1
            curSum += big
        return output
    
    
    def FindContinuousSequence2(self, tsum):
        if tsum < 3:
            return []
        small, big = 1, 2
        middle = (tsum + 1) >> 1
        curSum = small + big
        output = []
        while small < middle:
            if curSum == tsum:
                output.append(list(range(small, big+1)))
                big += 1
                curSum += big
            elif curSum > tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output


s = Solution()
print(s.FindContinuousSequence2(3))