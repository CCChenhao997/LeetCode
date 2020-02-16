"""
Reverse a singly linked list.

Example:
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        p1, p2, p3 = None, head, head.next
        while p2 != None:
            if not p2.next:
                p2.next = p1
                return p2
            p2.next = p1
            p1, p2, p3 = p2, p3, p3.next