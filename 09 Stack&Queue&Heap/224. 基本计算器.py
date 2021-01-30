'''
Description: 
version: 
Author: chenhao
Date: 2021-01-30 22:26:06
'''

"""
实现一个基本的计算器来计算一个简单的字符串表达式 s 的值。 

示例 1：
输入：s = "1 + 1"
输出：2

示例 2：
输入：s = " 2-1 + 2 "
输出：3

示例 3：
输入：s = "(1+(4+5+2)-3)+(6+8)"
输出：23

提示：
1 <= s.length <= 3 * 105
s 由数字、'+'、'-'、'('、')'、和 ' ' 组成
s 表示一个有效的表达式

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def calculate(self, s: str) -> int:
        s += '+'
        stack = []
        sign = 1
        operand = 0
        res = 0
        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            elif ch in {'+', '-', '(', ')'}:
                if ch == '+':
                    res += operand * sign
                    sign, operand = 1, 0
                elif ch == '-':
                    res += operand * sign
                    sign, operand = -1, 0
                elif ch == '(':
                    stack.append(res)
                    stack.append(sign)
                    sign, operand = 1, 0
                    res = 0
                elif ch == ')':
                    res += operand * sign
                    res *= stack.pop()  # sign
                    res += stack.pop()
                    operand = 0
        return res


if __name__ == '__main__':
    s = "(1+(4+5+2)-3)+(6+8)"
    so = Solution()
    print(so.calculate(s))