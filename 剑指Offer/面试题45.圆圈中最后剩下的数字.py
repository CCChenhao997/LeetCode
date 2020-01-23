"""
题目描述:
0, 1, 2, n-1这n个数字排成一个圆环, 从数字0开始每次从这个圆圈里删除第m个数字。
求这个圆圈中最后剩下的一个数字。

思路:
递推公式：f[i] = (f[i-1]+m)%i
"""

class Solution:
    def LastRemaining_Solution(self, n, m):
        if n < 1 or m < 1:
            return -1
        remainIndex = 0
        for i in range(1, n+1):
            remainIndex = (remainIndex + m) % i
        return remainIndex