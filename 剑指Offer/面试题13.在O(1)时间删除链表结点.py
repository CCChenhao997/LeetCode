'''
题目: 
给定单向链表的头指针和一个结点指针,定义一个函数在O(1)时间删除该结点

解题思路:
当要删除的结点不是尾结点而且不是仅有一个结点的头结点，可以把该结点i的下一个结点j的内容复制到结点i，
同时把i结点的next指向j结点的next，然后再删除结点j。如果要删除的链表为单结点链表且待删除的结点就
是头结点，需要把头结点置为None，如果删除的结点为链表的尾结点，那么就需要顺序遍历链表，找到尾节点
前面一个结点，然后将其next置空。
'''


class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None
    def __del__(self):
        self.val = None
        self.next = None
    
class Solution:
    def DeleteNode(self, pListHead, pToBeDeleted):
        if not pListHead or not pToBeDeleted:
            return None
        
        if pToBeDeleted.next != None:
            pNext = pToBeDeleted.next
            pToBeDeleted.val = pNext.val
            pToBeDeleted.next = pNext.next
            # 释放这个自己定义的结点
            pNext.__del__()

        # 头结点就是尾结点
        elif pListHead == pToBeDeleted:
            pListHead.__del__()
        
        # 删除的是尾结点
        else:
            pNode = pListHead
            while pNode.next != pToBeDeleted:
                pNode = pNode.next
            pNode.next = None
            pToBeDeleted.__del__()