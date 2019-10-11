'''
题目描述
大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39

思路：
如果 n 比较大，用递归就非常慢，而且存在效率问题。
不使用递归实现斐波那契数列，需要把前面两个数字存入在一个数组中。
'''


class Solution:
    def Fibonacci(self, n):
        tempArray = [0, 1]
        i = n
        if n >= 2:
            for i in range(2, n+1):
                tempArray[i%2] = tempArray[0] + tempArray[1]
        return tempArray[i%2]


test = Solution()
print(test.Fibonacci(100))