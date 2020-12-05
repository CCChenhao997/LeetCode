"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        lenOfLink1, lenOflink2 = 1, 1
        link1, link2 = headA, headB
        while link1.next:
            lenOfLink1 += 1
            link1 = link1.next
        while link2.next:
            lenOflink2 += 1
            link2 = link2.next
        diff = abs(lenOfLink1 - lenOflink2)
        while diff:
            if lenOfLink1 > lenOflink2:
                headA = headA.next
            else:
                headB = headB.next
            diff -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA
    
    def getIntersectionNode2(self, headA: ListNode, headB: ListNode) -> ListNode:
        # 利用 a + c + b = b + c + a 思路
        link1, link2 = headA, headB
        while link1 != link2:
            link1 = link1.next if link1 else headB
            link2 = link2.next if link2 else headA
        return link1