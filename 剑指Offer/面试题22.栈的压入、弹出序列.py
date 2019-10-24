'''
题目描述
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列
是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。例如序
列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应
的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

思路:
建立一个辅助栈，把push序列的数字依次压入辅助栈，每次压入后，比较
辅助栈的栈顶元素和pop序列的首元素是否相等，相等的话就推出pop序列
的首元素和辅助栈的栈顶元素，若最后辅助栈为空，则push序列可以对应
于pop序列。
'''

class Solution:
    # 方法一
    def IsPopOrder(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        
        stack = []
        for i in pushV:
            stack.append(i)
            if stack[-1] != popV[0]:  
                continue
            else:  # 若输入序列的数字等于输出序列的首数字，则都pop
                stack.pop()
                popV.pop(0)
        while len(stack) > 0 and stack[-1] == popV[0]:
            stack.pop()
            popV.pop(0)
        
        if len(stack) == 0:
            return True
        else:
            return False

    # 方法二：优化
    def IsPopOrder2(self, pushV, popV):
        if pushV == [] or popV == []:
            return False
        stack = []
        for i in pushV:
            stack.append(i)
            while len(stack) and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        if len(stack):
            return False
        else:
            return True


pushV = [1, 2, 3, 4, 5]
popV = [4, 5, 3, 2, 1]
popVF = [4, 5, 2, 1, 3]
S = Solution()
print(S.IsPopOrder(pushV, popV))