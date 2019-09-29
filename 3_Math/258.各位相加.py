'''
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:
输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-digits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


"""
# 解法一: 循环
class Solution:
    def addDigits(self, num: int) -> int:
        if num < 10:
            return num

        num_str = str(num)
        num_len = len(num_str)
        while num_len > 1:
            num = 0
            for i in num_str:
                num += int(i)
            num_str = str(num)
            num_len = len(num_str)
        
        return num
"""

"""
# 解法二: python 特色解法
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = eval('+'.join(n for n in str(num)))
        return num
"""


# 解法三: 复杂度 O(1)
'''
O(1) 数学推理：设某个数字的字符串表示为'abc'，则这个数字代表a*100 + b*10 + c，转换后成为a + b + c，
可见每次转换相当于把原数字减去a*99 + b*9 = 9 * (a*11 + b)，可以推出只要高于个位的位置上有数字，算法
就会减去一个小于原数字的9的倍数，这就相当于数字 % 9。但9 % 9 = 0，而 9 本身就没有十位，因此需要考虑原
数字是 0 或 9 的倍数的特殊情况

首先计算num % 9，若结果为 0 则考虑num本身是否为 0，若不为 0 返回 9
'''
class Solution:
    def addDigits(self, num: int) -> int:
        return num % 9 or 9 * bool(num)


if __name__=='__main__':
    X = Solution()
    num = 38
    print(X.addDigits(num))