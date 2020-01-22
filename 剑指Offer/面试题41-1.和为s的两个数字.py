"""
题目描述：
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。

思路：
两个指针从左到右和从右到左遍历
"""

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        if array == None or len(array) <= 0 or array[-1] + array[-2] < tsum:
            return []
        i, j = 0, len(array) - 1
        while i <= j:
            Asum = array[i] + array[j]
            if Asum == tsum:
                return [array[i], array[j]]
            elif Asum > tsum:
                j -= 1
            else:
                i += 1
        return []