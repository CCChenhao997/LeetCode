'''
@Description: 
@version: 
@Author: chenhao
@Date: 2020-04-21 23:21:40
@LastEditors: chenhao
@LastEditTime: 2020-04-21 23:56:37
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper =[]

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)
        else:
            self.helper.append(self.helper[-1])

    def pop(self) -> None:
        if self.data:
            self.helper.pop()
            return self.data.pop()

    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]
        
        
class MinStack1:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = []
        self.helper =[]

    def push(self, x: int) -> None:
        self.data.append(x)
        if len(self.helper) == 0 or x <= self.helper[-1]:
            self.helper.append(x)

    def pop(self) -> None:
        top = self.data.pop()
        if self.helper and top == self.helper[-1]:
            self.helper.pop()
        return top
        
    def top(self) -> int:
        if self.data:
            return self.data[-1]

    def getMin(self) -> int:
        if self.helper:
            return self.helper[-1]