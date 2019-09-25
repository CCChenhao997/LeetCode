'''
丑数就是只包含质因数 2, 3, 5 的正整数。

示例 1:
输入: 6
输出: true
解释: 6 = 2 × 3

示例 2:
输入: 8
输出: true
解释: 8 = 2 × 2 × 2

示例 3:
输入: 14
输出: false 
解释: 14 不是丑数，因为它包含了另外一个质因数 7。

说明：
1 是丑数。
输入不会超过 32 位有符号整数的范围: [−231,  231 − 1]。
在真实的面试中遇到过这道题？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/ugly-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

"""
# 解法一：循环实现
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False
        while True:
            if num == 1:
                return True
            if num % 2 == 0:
                num = num // 2
            elif num % 3 == 0:
                num = num // 3
            elif num % 5 == 0:
                num = num // 5
            else:
                break
        return False
"""


# 解法二: 递归
class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0: return False
        if num == 1: return True
        if num % 2 == 0: return self.isUgly(num // 2)
        if num % 3 == 0: return self.isUgly(num // 3)
        if num % 5 == 0: return self.isUgly(num // 5)
        return False


"""
# 解法二: 迭代
class Solution:
    def isUgly(self, num: int) -> bool:
        for p in 2, 3, 5:
            while num % p == 0 < num:
                num //= p
        return num == 1
"""

if __name__=='__main__':
    X = Solution()
    num = 10
    print(X.isUgly(num))