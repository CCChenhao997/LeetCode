"""
题目描述:
随机从扑克牌中抽出了5张牌,判断是不是顺子,
大/小王可以看成任何数字,并且A看作1,J为11,Q为12,K为13。

思路:
先置换特殊字符AJQK为数字，排序，然后求出大小王即0的个数，然后求出除去0之外的，
数组间的数字间隔(求间隔的时候记得减去1，比如4和5的间隔为5-4-1，表示4和5是连续的数字)，
同时求间隔的时候需要鉴别是否出现对。最后比较0的个数和间隔的大小即可。
"""

class Solution:
    def IsContinuous(self, numbers):
        if numbers == None or len(numbers) <= 0:
            return False
        # 把A、J、Q、K转化为数字
        transDict = {'A':1, 'J':11, 'Q':12, 'K':13}
        for i in range(len(numbers)):
            if numbers[i] in transDict.keys():
                numbers[i] = transDict[numbers[i]]
        numbers.sort()
        numberOfZero = 0
        numberOfGap = 0
        
        # 统计0的个数
        for i in numbers:
            if i == 0:
                numberOfZero += 1
        
        # 统计间隔的数目
        small = numberOfZero
        big = small + 1
        while big < len(numbers):
            # 出现对子，不可能是顺子
            if numbers[small] == numbers[big]:
                return False
            numberOfGap += numbers[big] - numbers[small] - 1
            small = big
            big += 1
        return False if numberOfGap > numberOfZero else True


test = ['A', 3, 2, 5, 0]
test2 = [0, 3, 1, 6, 4]
s = Solution()
print(s.IsContinuous(test))