'''
题目描述
输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
（不准改变链表结构）

思路：
1. 使用栈
2. 递归
'''

# -*- coding:utf-8 -*-
class listNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法一：使用栈
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode.val == None:
            return
        stack = []
        head = listNode
        while head:
            stack.insert(0, head.val)
            head = head.next
        return stack
        