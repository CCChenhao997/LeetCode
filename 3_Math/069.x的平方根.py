'''
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:
输入: 4
输出: 2

示例 2:
输入: 8
输出: 2
说明: 8 的平方根是 2.82842..., 
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# 解法一: 自己的暴力循环法
class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(1, x+1):
            r = x // i
            if r <= i:
                return int(r)
"""


# 解法二: 二分查找 （碰到这种要遍历的，就要想到用二分查找）
class Solution:
    def mySqrt(self, x: int) -> int:
        l, h = 0, x
        while l < h:
            m = (l + h) // 2
            if m**2 <= x < (m+1)**2:
                return m
            elif m**2 < x:
                l = m + 1
            else:
                h = m - 1
        return l


if __name__=='__main__':
    X = Solution()
    x = 9
    print(X.mySqrt(x))