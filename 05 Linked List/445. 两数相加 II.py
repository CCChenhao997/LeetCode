'''
Description: 
version: 
Author: chenhao
Date: 2021-02-01 16:35:15
'''

"""
给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例：
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # * 对于逆序处理，首先应该想到栈
        stack_l1, stack_l2 = [], []
        while l1:
            stack_l1.append(l1.val)
            l1 = l1.next
        while l2:
            stack_l2.append(l2.val)
            l2 = l2.next
        
        carry = 0
        pre = None
        while stack_l1 or stack_l2 or carry > 0:
            v1 = stack_l1.pop() if stack_l1 else 0
            v2 = stack_l2.pop() if stack_l2 else 0
            tmp = v1 + v2 + carry
            p = ListNode(tmp % 10)
            p.next = pre
            pre = p
            carry = tmp // 10
        
        return pre