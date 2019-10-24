'''
题目描述
定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素
的min函数（时间复杂度应为O(1)）

思路：
引入两个栈，一个栈每次push实际的数字，如果push的数字小于minStack
栈顶的数字或者minStack为空，则将该数字也push到minStack，否则，将
minStack栈顶的数字再压入一遍。
'''


class Solution:
    def __init__(self):
        self.stack = []
        self.minStack = []
    def push(self, node):
        self.stack.append(node)
        if self.minStack == [] or node < self.min():
            self.minStack.append(node)
        else:
            temp = self.min()
            self.minStack.append(temp)
    def pop(self):
        if self.stack == [] or self.minStack == []:
            return None
        self.minStack.pop()
        self.stack.pop()
    def top(self):
        return self.stack[-1]
    def min(self):
        return self.minStack[-1]


S = Solution()
S.push(3)
S.push(4)
S.push(2)
S.push(1)
print(S.min())
S.pop()
print(S.min())