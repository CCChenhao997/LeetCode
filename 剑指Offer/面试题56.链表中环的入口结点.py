"""
题目描述:
给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。

思路:
寻找链表中环的入口结点主要分成三个步骤：
首先是设置两个快慢指针，如果快慢指针相遇，则快慢指针必然都在环中；
然后从相遇的地方设置一个指针向后遍历并记录走的步数，当这个指针重新指到开始的位置的时候，
当前对应的步数就是环中结点的数量k；然后设置两个指针从链表开始，第一个节点先走k步，
然后第二个指针指到链表的开始，两个指针每次都向后走一步，两个指针相遇的位置就是链表的入口。
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
         
class Solution:
    def EntryNodeOfLoop(self, pHead):
        meetingNode = self.MeetingNode(pHead)
        if not meetingNode:
            return None
        NodeLoop = 1
        flagNode = meetingNode
        while flagNode.next != meetingNode:
            NodeLoop += 1
            flagNode = flagNode.next
        pFast = pHead
        for i in range(NodeLoop):
            pFast = pFast.next
        pSlow = pHead
        while pFast != pSlow:
            pFast = pFast.next
            pSlow = pSlow.next
        return pFast
        
    def MeetingNode(self, pHead):
        if pHead == None:
            return None
        pSlow = pHead.next
        if pSlow == None:
            return None
        pFast = pSlow.next
        while pFast:
            if pSlow == pFast:
                return pSlow
            pSlow = pSlow.next
            pFast = pFast.next
            if pFast:
                pFast = pFast.next


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node3

s = Solution()
print(s.EntryNodeOfLoop(node1).val)