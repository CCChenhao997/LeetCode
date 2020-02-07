"""
题目描述:
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。

思路:
构建一个最大堆和一个最小堆，分别存储比中位数小的数和大的数。
当目前两堆总数为偶数的时候，把数字存入最大堆，然后重排最大堆，
如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，
重排两堆，此时两堆数字总数为奇数，直接输出最大堆堆顶数字即为中位数；
如果当前两堆总数为奇数的时候，把数字存入最小堆，重排最小堆，
如果最大堆的堆顶数字大于最小堆堆顶数字，则把两个堆顶数字交换，
重排两堆，此时两堆数字总数为偶数，取两堆堆顶数字做平均即为中位数。
"""

from heapq import *

class Solution:
    def __init__(self):
        self.small = []
        self.large = []
    
    def Insert(self, num):
        small, large = self.small, self.large
        heappush(small, -heappushpop(large, -num))
        if len(large) < len(small):
            heappush(large, -heappop(small))
    
    def GetMedian(self, n=1):
        small, large = self.small, self.large
        if len(large) > len(small):
            return -large[0]
        return (small[0] - large[0]) / 2.0
    

class Solution2:
    def __init__(self):
        self.l = []
    def Insert(self, num):
        # write code here
        self.l.append(num)
        self.l.sort()
         
    def GetMedian(self,l):
        # write code here
        n = len(self.l)
        if n%2==1:
            return self.l[n//2]
        else:
            return (self.l[n//2-1]+self.l[n//2])/2.0
