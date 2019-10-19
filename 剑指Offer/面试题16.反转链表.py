'''
题目描述:
输入一个链表，反转链表后，输出新链表的表头。

解题思路:
需要注意三个问题：输入的链表头指针为None或者整个链表只有一个结点时，
反转后的链表出现断裂，返回的翻转之后的头节点不是原始链表的尾结点。
因此需要引入一个翻转后的头结点，以及一个指向当前结点的指针，一个
指向当前结点前一个结点的指针，一个指向当前结点后一个结点的指针，
防止出现断裂。
推广：递归实现反转链表
'''


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        pReversedHead = None
        pNode = pHead
        pPrev = None
        while pNode != None:
            pNext = pNode.next

            if pNext == None:
                pReversedHead = pNode

            pNode.next = pPrev
            pPrev = pNode
            pNode = pNext
        return pReversedHead

    # 递归实现反转链表
    # 图解: https://blog.csdn.net/FX677588/article/details/72357389
    def ReverseListRecursive(self, pHead):
        if not pHead or not pHead.next:
            return pHead
        else:
            pReversedHead = self.ReverseListRecursive(pHead.next)
            pHead.next.next = pHead
            pHead.next = None
            return pReversedHead