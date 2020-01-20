"""
题目描述：
输入两个链表，找出它们的第一个公共结点。

思路：
首先依次遍历两个链表，记录两个链表的长度m和n，如果 m > n，那么我们就先让长度为m的链表走m-n个结点，然后两个链表同时遍历，当遍历到相同的结点的时候停止即可。对于 m < n，同理。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        nLength1 = self.GetListLength(pHead1)
        nLength2 = self.GetListLength(pHead2)
        nLengthDiff = abs(nLength1 - nLength2)
        if nLength1 > nLength2:
            pListHeadLong = pHead1
            pListHeadShort = pHead2
        else:
            pListHeadLong = pHead2
            pListHeadShort = pHead1
        for i in range(nLengthDiff):
            pListHeadLong = pListHeadLong.next
        while pListHeadLong != None and pListHeadShort != None and pListHeadLong != pListHeadShort:
            pListHeadLong = pListHeadLong.next
            pListHeadShort = pListHeadShort.next
        return pListHeadLong
        
    def GetListLength(self, pHead):
        nLength = 0
        while pHead != None:
            pHead = pHead.next
            nLength += 1
        return nLength