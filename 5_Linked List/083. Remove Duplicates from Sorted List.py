"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:
Input: 1->1->2
Output: 1->2

Example 2:
Input: 1->1->2->3->3
Output: 1->2->3
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        p = head
        while p:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head
    
    # 递归没看懂
    def deleteDuplicates2(self, head):
        if not head or not head.next:
            return head
        head.next = self.deleteDuplicates2(head.next)
        return head.next if head.val == head.next.val else head