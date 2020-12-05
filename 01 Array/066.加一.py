'''
给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。
你可以假设除了整数 0 之外，这个整数不会以零开头。
示例 1:
输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。
示例 2:
输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。
链接：https://leetcode-cn.com/problems/plus-one
'''

'''
# 解法一: 自己写的
class Solution:
    def plusOne(self, digits):
        digits2str = [str(i) for i in digits]       # 把数字列表变成字符列表
        new_digits = int(''.join(digits2str)) + 1   # digit+1的数值
        return [i for i in str(new_digits)]
'''

# 解法二: 更快一点
class Solution:
    def plusOne(self, digits):
        sums = 0
        for i in range(len(digits)):
            sums += 10**(len(digits)-1-i) * digits[i]
        sum_str = str(sums + 1)
        return [int(j) for j in sum_str]



if __name__=='__main__':
    digits = [4,3,2,1]
    X = Solution()
    print(X.plusOne(digits))