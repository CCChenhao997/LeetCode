'''
给定一个整数，编写一个函数来判断它是否是 2 的幂次方。

示例 1:
输入: 1
输出: true
解释: 2^0 = 1

示例 2:
输入: 16
输出: true
解释: 2^4 = 16

示例 3:
输入: 218
输出: false

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# 解法一: 还行，时间复杂度超过99.87%
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        if n == 1: return True
        if n < 0: return False
        while n > 1:
            r = n / 2
            if r != int(r):
                return False
            else:
                n = r
        return True
"""

# 解法二: 位运算
'''
解题思路：
若 n = 2^x 且 x 为自然数（即 n 为 2 的幂），则一定满足以下条件：
    1. 恒有 n & (n - 1) == 0，这是因为：
        - n 二进制最高位为 1，其余所有位为 0；
        - n - 1 二进制最高位为 0，其余所有位为 1；
    2. 一定满足 n > 0。
因此，通过 n > 0 且 n & (n - 1) == 0 即可判定是否满足 n = 2^x。
'''
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0



if __name__=='__main__':
    X = Solution()
    n = 16
    print(X.isPowerOfTwo(n))

