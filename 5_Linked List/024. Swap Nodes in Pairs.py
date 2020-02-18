"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.

Example:
Given 1->2->3->4, you should return the list as 2->1->4->3.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy, dummy.next = ListNode(0), head
        p1 = dummy
        p2, p3 = p1.next, p1.next.next
        
        while p2 and p3:
            
            p1.next = p3
            p2.next = p3.next
            p3.next = p2
        
            # p1 = p1.next.next
            p1 = p2
            p2, p3 = p1.next, p1.next.next
            
        return dummy.next
        