"""
题目描述：
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。

思路：
将两个数的加法看作两步，第一步是两个数相加但是不进位，第二步是记录之前的两数相加应该进位的地方
加上前一个相加但是不进位的数。对于具体的两个不小于0的数m和n，第一步可以看做m和n的异或运算m^n，
第二步可以看做m和n的与运算然后左移一位得到实际的进位位置(m&n)<<1。然后把两个得到的数字加起来
继续操作，指到carry进位为0终止操作。
"""

# step1:按位与是查看两个数哪些二进制位都为1，这些都是进位位，结果需左移一位，表示进位后的结果
# step2:异或是查看两个数哪些二进制位只有一个为1，这些是非进位位，可以直接加、减，结果表示非进位位进行加操作后的结果
# step3:n1&n2是查看有没有进位位了，如果有，需要重复step1、step2；如果没有，保留n1、n2上二进制为1的部分，用或将之合为一个数，即为最后结果
# 首先看十进制是如何做的： 5+7=12，三步走
# 第一步：相加各位的值，不算进位，得到2。
# 第二步：计算进位值，得到10. 如果这一步的进位值为0，那么第一步得到的值就是最终结果。
# 第三步：重复上述两步，只是相加的值变成上述两步的得到的结果2和10，得到12。
# 同样我们可以用三步走的方式计算二进制值相加： 5-101，7-111 第一步：相加各位的值，不算进位，得到010，二进制每位相加就相当于各位做异或操作，101^111。
# 第二步：计算进位值，得到1010，相当于各位做与操作得到101，再向左移一位得到1010，(101&111)<<1。
# 第三步重复上述两步， 各位相加 010^1010=1000，进位值为100=(010&1010)<<1。
#      继续重复上述两步：1000^100 = 1100，进位值为0，跳出循环，1100为最终结果。

class Solution:
    def Add(self, num1, num2):
        # n1 = (num1 & num2) << 1
        # n2 = num1 ^ num2
        # while n1 & n2:  # 判断是否还有进位
        #     num1, num2 = n1, n2
        #     n1 = (num1 & num2) << 1
        #     n2 = num1 ^ num2
        # return n1 | n2
        while num2 != 0:
            temp = num1 ^ num2
            num2 = (num1 & num2) << 1
            num1 = temp & 0xFFFFFFFF
        return num1 if num1 >> 31 == 0 else num1 - 4294967296
    

s = Solution()
print(s.Add(-5, 7))