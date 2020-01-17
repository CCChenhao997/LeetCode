"""
题目描述：
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4。
"""

class Solution:
    # O(n)的算法，只有当我们可以修改输入的数组时可用
    # 基于Partition的方法
    def GetLeastNumbers_Solution(self, tinput, k):
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        n = len(tinput)
        start = 0
        end = n - 1
        index = self.Partition(tinput, n, start, end)
        while index != k-1:
            if index > k-1:
                end = index - 1
                index = self.Partition(tinput, n, start, end)
            else:
                start = index + 1
                index = self.Partition(tinput, n, start, end)
        output = tinput[:k]
        output.sort()
        return output
    
    def Partition(self, numbers, length, start, end):
        import random
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None  
        index = random.randint(start, end)   
        numbers[index], numbers[end] = numbers[end], numbers[index]   # 将index位置的数移动到最后一位
        small = start - 1
        for index in range(start, end):
            if numbers[index] < numbers[end]:  #index位置表示的是当前的数，small表示的是小于区域
                small += 1
                if small != index:
                    numbers[index], numbers[small] = numbers[small], numbers[index]  # 永远将小于end的index放进small区域
        small += 1   # for循环出来以后小于"end"的都在small区域，因此需要再做一次变换将end放到small+1的位置，变成small到"end"区域的局部有序
        numbers[small], numbers[end] = numbers[end], numbers[small]
        return small
    
    # O(nlogk)的算法, 适合海量数据
    # 利用一个k容量的容器存放数组，构造最大堆。当下一个数大于最大数，跳过；小于最大数，则进入容器替换之前的最大数。
    def GetLeastNumbers(self, tinput, k):
        import heapq
        if tinput == None or len(tinput) < k or len(tinput) <= 0 or k <= 0:
            return []
        output = []
        for number in tinput:
            if len(output) < k:
                output.append(number)
            else:
                output = heapq.nlargest(k, output)
                if number >= output[0]:
                    continue
                else:
                    output[0] = number
        output = heapq.nlargest(k, output)
        return output[::-1]
    
    

tinput = [4,5,6,2,7,3,8,1]
s = Solution()
print(s.GetLeastNumbers_Solution(tinput, 2))
# print(s.GetLeastNumbers(tinput, 2))