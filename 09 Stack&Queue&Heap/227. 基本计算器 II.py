'''
Description: 
version: 
Author: chenhao
Date: 2021-01-30 12:43:31
'''

"""
实现一个基本的计算器来计算一个简单的字符串表达式的值。
字符串表达式仅包含非负整数，+， - ，*，/ 四种运算符和空格  。 整数除法仅保留整数部分。

示例 1:
输入: "3+2*2"
输出: 7

示例 2:
输入: " 3/2 "
输出: 1

示例 3:
输入: " 3+5 / 2 "
输出: 5

说明：
你可以假设所给定的表达式都是有效的。
请不要使用内置的库函数 eval。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def calculate(self, s: str) -> int:
        s += '+'    # 防止最后一个数漏掉计算
        stack = []
        operand = 0
        sign = '+'
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            if ch in {'+', '-', '*', '/'}:
                if sign == '+':
                    stack.append(operand)
                elif sign == '-':
                    stack.append(-operand)
                elif sign == '*':
                    stack[-1] = stack[-1] * operand
                elif sign == '/':
                    stack[-1] = stack[-1] // operand if stack[-1] > 0 \
                                else -(-stack[-1] // operand)
                sign = ch
                operand = 0
        return sum(stack)
    

if __name__ == '__main__':
    s = "3+2*2"
    so = Solution()
    print(so.calculate(s))