'''
题目描述
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1(self, n):
        counter = 0
        # print("n", bin(n))
        if n < 0:
            # 负数在计算机中存储的是补码形式，不过python输出的负数二进制并不是补码形式
            # 所以将计算机中的负数跟0xffffffff(全1)相与，就得到了负数的补码形式
            n = n & 0xffffffff  # 得到一个整数，这个正数的补码和原来负数的形式一样
            # print("n", bin(n))
        while n:
            counter += 1
            # 把一个整数减去1，再和原来整数做与运算，会把该整数最右边一个1变成0.
            n = (n-1) & n
        return counter

    def NumberOf2(self, n):
        if n < 0:
            s = bin(n & 0xffffffff)
        else:
            s = bin(n)
        return s.count('1')

    '''
    扩展
    '''
    # 判断一个数是不是2的整数次幂
    def powerOf2(self, n):
        if n & (n-1) == 0:
            return True
        else:
            return False
    
    # 判断两个数的二进制表示有多少位不一样，直接比较两个数的二进制异或就可
    def andOr(self, m, n):
        # ^ 是异或操作符
        # 异或 计算出m和n之间不同的个数
        diff = m ^ n
        count = 0
        # 统计异或中1的个数
        while diff:
            count += 1
            diff = diff & (diff - 1)
        return count



test = Solution()
print(test.NumberOf1(-9))

print(bin(-9))
print(bin(-9&8))