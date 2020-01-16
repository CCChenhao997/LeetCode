"""
数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。
"""

"""
方法一：基于Partition函数的O(n)算法
    由于当前数组是非排序的，所以需要先进行排序，O(nlogn)；
    对于有序数组来说，中位数即 n/2 位置上的数字一定是频率超过一半的数字；
    按照快速排序的思想，
        选择一个基准pivot；
        将小于pivot的数字放在 pivot 左边，将大于pivot的数字放在 pivot 右边；
        如果本轮 pivot 的索引大于 n/2 ，则寻找的目标在 pivot 左边；否则，在 pivot 右边。
    判断特殊情况：
        输入数组为空；
        不存在频率超过一半的数字。

方法二：根据数组特点找出O(n)的算法
数组中有一个数字出现的次数超过数组长度的一半，也就是说它出现的次数比其他所有数字出现次数的和还要多。因此我们可以考虑在遍历数组的时候保存两个值：
    一个是数组中的一个数字，
    一个是次数。
    当我们遍历到下一个数字的时候，如果下一个数字和我们之前保存的数字相同，则次数加1；
    如果下一个数字和我们之前保存的数字不同，则次数减1。
    如果次数为零，我们需要保存下一个数字，并把次数设为1。
    由于我们要找的数字出现的次数比其他所有数字出现的次数之和还要多，那么要找的数字肯定是最后一次把次数设为1时对应的数字。
"""

import random

class Solution:
    
    # 解法一: 基于Partition函数的O(n)算法
    def MoreThanHalfNum_Solution(self, numbers):
        length = len(numbers)
        if length == 1:
            return numbers[0]
        if self.CheckInvalidArray(numbers, length):
            return 0
        
        middle = length >> 1
        start = 0
        end = length - 1
        index = self.Partition(numbers, length, start, end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(numbers,length, start, end)
            else:
                start = index + 1
                index = self.Partition(numbers, length, start, end)
        result = numbers[middle]
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result
    
    # Partition 算法
    def Partition(self, numbers, length, start, end):
        if numbers == None or length <= 0 or start < 0 or end >= length:
            return None  # 正常这里应该是抛出异常
        index = random.randint(start, end)   # 生成一个start和end之间的一个整数
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
    
    # 检查输入的数组是否合法
    def CheckInvalidArray(self, numbers, length):
        InputInvalid = False
        if numbers == None or length <= 0:
            InputInvalid = True
        return InputInvalid
    
    # 检查查找到中位数的元素出现次数是否超过所有元素数量的一半
    def CheckMoreThanHalf(self, numbers, length, number):
        times = 0
        for i in range(length):
            if numbers[i] == number:
                times += 1
        if times * 2 <= length:
            return False
        return True
    
    # 解法二: 根据数组特点找出O(n)的算法
    def MoreThanHalfNum(self, numbers):
        length = len(numbers)
        if numbers == None or length <= 0:
            return 0
        result = numbers[0]
        times = 1
        for i in range(1, length):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times += 1
            else:
                times -= 1
        if not self.CheckMoreThanHalf(numbers, length, result):
            result = 0
        return result
                


S = Solution()
print(S.MoreThanHalfNum_Solution([1, 2, 3, 2, 2, 2, 5, 4, 2]))
print(S.MoreThanHalfNum_Solution([1, 2, 3, 3, 3, 3, 4]))
print(S.MoreThanHalfNum_Solution([1, 2]))
print(S.MoreThanHalfNum_Solution([4,2,1,4,2,4]))
# print(S.MoreThanHalfNum([1, 2, 3, 2, 2, 2, 5, 4, 2]))
# print(S.MoreThanHalfNum([1, 2, 3, 3, 3, 3, 4]))
# print(S.MoreThanHalfNum([1, 2]))