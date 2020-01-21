"""
题目描述:
统计一个数字在排序数组中出现的次数。

思路:
二分查找
"""

class Solution:
    def GetNumberOfK(self, data, k):
        number = 0
        if data != None and len(data) > 0:
            length = len(data)
            first = self.GetFirstK(data, k, 0, length-1)
            last = self.GetLastK(data, k, 0, length-1)
            if first > -1:
                number = last - first + 1
        return number
    
    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        middleIndex = (start + end) // 2
        middleData = data[middleIndex]
        if middleData == k:
            if middleIndex > 0 and data[middleIndex-1] == k:
                end = middleIndex - 1
            else:
                return middleIndex
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetFirstK(data, k, start, end)
    
    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        middleIndex = (start + end) // 2
        middleData = data[middleIndex]
        if middleData == k:
            if middleIndex < end and data[middleIndex+1] == k:
                start = middleIndex + 1
            else:
                return middleIndex
        elif middleData > k:
            end = middleIndex - 1
        else:
            start = middleIndex + 1
        return self.GetLastK(data, k, start, end)
    
aList = [1, 2, 3, 3, 3, 3, 4, 5]
s = Solution()
print(s.GetNumberOfK(aList, 3))