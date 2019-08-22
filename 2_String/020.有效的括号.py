'''
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：
    1.左括号必须用相同类型的右括号闭合。
    2.左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true

链接：https://leetcode-cn.com/problems/valid-parentheses
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        judge = {'()', '[]', '{}'}
        for i in s:
            if not stack:   # 如果stack是空的
                stack.append(i)
            else:           # stack不是空的
                if stack[-1] + i in judge:
                    stack.pop()
                else:
                    stack.append(i)

        return stack == []


if __name__=='__main__':
    X = Solution()
    # s = "()"
    s = "{[]}"
    print(X.isValid(s))
