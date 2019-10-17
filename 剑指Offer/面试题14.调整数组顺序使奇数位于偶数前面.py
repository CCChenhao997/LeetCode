'''
题目描述:
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的
后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。

思路：
注重函数的扩展性能。把函数中的判断条件写成一个判断条件的
函数，方便与函数的扩展。对于奇数位于偶数前面的情况，类似
于快排，在头和尾分别设置一个指针，头指针指向奇数则后移，
尾指针指向偶数则前移。
'''

class Solution:
    # 如果不要求保证奇数和奇数，偶数和偶数之间的相对位置不变，则这种解法可以
    def reOrderArray(self, array):
        if len(array) < 1:
            return
        elif len(array) == 1:
            return array
        
        front = 0               # 第一个指针
        rear = len(array) - 1   # 第二个指针
        while front <= rear:
            while array[front] & 0x1 == 1:  # 如果是奇数
                front += 1      # front指针向后走一个
                # print("front走一次")
            while array[rear] & 0x1 == 0:   # 如果是偶数
                rear -= 1       # rear指针向前走一个
                # print("rear走一次")
            # 当front遇到偶数，rear遇到奇数，交换
            # print("array[front]",array[front])
            # print("array[rear]",array[rear])
            array[front], array[rear] = array[rear], array[front]
            front += 1
            rear -= 1
            # print("交换后")
            # print("array[front]",array[front])
            # print("array[rear]",array[rear])
        # array[front], array[rear] = array[rear], array[front]
        return array


    # 利用Python的trick，写一个简单的排列数组，顺序不变
    def reOrderArray1(self, array):
        left = [x for x in array if x & 1]
        right = [x for x in array if not x & 1]
        return left + right
    

    def reOrderArray2(self,array):
        if len(array) < 1:
            return []
        if len(array) == 1:
            return array
        arrayOdd = []
        arrayEven = []
        for num in array:
            if num & 0x1:
                arrayOdd.append(num)
            else:
                arrayEven.append(num)
        return arrayOdd + arrayEven

    
    # 可扩展性的解法
    # 注意在一个函数的输入中，输入另一个函数的写法func = self.funcName, funcName不需要加括号
    def Reorder(self, pData, length, func):
        if length == 0:
            return
        
        pBegin = 0
        pEnd = length - 1

        while pBegin < pEnd:
            while pBegin < pEnd and not func(pData[pBegin]):
                pBegin += 1
            while pBegin < pEnd and func(pData[pEnd]):
                pEnd -= 1
            
            if pBegin < pEnd:
                pData[pBegin], pData[pEnd] = pData[pEnd], pData[pBegin]
        return pData
    
    def isEven(self, n):
        return not n & 0x1
    
    def isNegative(self, n):
        return n >= 0
    
    def ReorderOddEven(self, pData):
        length = len(pData)
        return self.Reorder(pData, length, func=self.isNegative)

    


test = Solution()
print(test.ReorderOddEven([-1, 2, -3, 4, -5, -6, 7, 8, 9, 10, -10]))